#!/usr/bin/env python
from datetime import timedelta

import pendulum
from jinja2 import BaseLoader
from jinja2.sandbox import SandboxedEnvironment

from aafclient import AAFClient
from helpers import pr_filter
from redditdata import subreddits

TEMPLATE = """
{% for game in games %}
## {{ game.away_team_edge.node.name }} @ {{ game.home_team_edge.node.name }}

| Player | Comp | Att | Yds | TD | Int | Rate |
|:-------|-----:|----:|----:|---:|----:|-----:|
{% for player in game.players_connection.edges %}
{% set p=player.node %}
{% set t=player.team %}
{% set s=player.stats %}
{% if player.stats.passes_attempted > 0 %}
| [*{{ t.abbreviation }}*](/r/{{ subreddits[t.abbreviation] }}) {{ p.legal_name.given_name }} {{ p.legal_name.family_name }} | {{ s.passes_completed }} | {{ s.passes_attempted }} | {{ s.passing_yards }} | {{ s.passing_touchdowns }} | {{ s.passes_intercepted }} | {{ s|passerrating }} |
{% endif %}
{% endfor %}

{% endfor %}

{% for game in games %}
{% for player in game.players_connection.edges %}
{% set p=player.node %}
{% set t=player.team %}
{% set s=player.stats %}
{% if player.stats.passes_attempted > 0 %}
    {{ p.legal_name.given_name }} {{ p.legal_name.family_name }},{{ t.abbreviation }},{{ s.passes_completed }},{{ s.passes_attempted }},{{ s.passing_yards }},{{ s.passing_touchdowns }},{{ s.passes_intercepted }},{{ s|passerrating }}
{% endif %}
{% endfor %}
{% endfor %}

""".strip()


def main():
    aaf = AAFClient('passerratings')

    now = pendulum.now()
    games = aaf.games_between(now - timedelta(days=7), now)

    env = SandboxedEnvironment(loader=BaseLoader(), trim_blocks=True)
    env.filters['passerrating'] = pr_filter
    template = env.from_string(TEMPLATE)
    print(template.render(games=games, subreddits=subreddits))


if __name__ == '__main__':
    main()
