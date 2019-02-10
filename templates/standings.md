# Standings

{% for division, teams in divisions.items() %}
## {{ division.name }}

| Team | W | L | PCT |
|:-----|--:|--:|----:|
{% for team in teams -%}
{%- if team.stats.games_played > 0 -%}
{%- set pct=team.stats.games_won / team.stats.games_played -%}
{%- else -%}
{%- set pct=0 -%}
{%- endif -%}
| [{{ team.nickname }}](/r/{{team.subreddit}}) | {{ team.stats.games_won }} | {{ team.stats.games_lost }} | {{ "%0.3f"|format(pct) }} |
{% endfor -%}
{%- endfor -%}
