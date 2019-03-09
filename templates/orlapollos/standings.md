{% set ourdivision = 'East' -%}
{% set ourteam = 'ORL' -%}
{% for division, teams in divisions.items() -%}
{% if division.name == ourdivision -%}
# {{ division.name }} Standings

| Team | W | L | T | PCT |
|:-----|--:|--:|--:|----:|
{% for team in teams -%}
{%- if team.stats.games_played > 0 -%}
{%- set pct=(team.stats.wins + 0.5 * team.stats.ties ) / team.stats.games_played -%}
{%- else -%}
{%- set pct=0 -%}
{%- endif -%}
{% if team.abbreviation == ourteam -%}
| [**{{ team.nickname }}**](/r/{{team|team_sr}}) | **{{ team.stats.wins }}** | **{{ team.stats.losses }}** | **{{ team.stats.ties }}** | **{{ "%0.3f"|format(pct) }}** |
{% else -%}
| [{{ team.nickname }}](/r/{{team|team_sr}}) | {{ team.stats.wins }} | {{ team.stats.losses }} | {{ team.stats.ties }} | {{ "%0.3f"|format(pct) }} |
{% endif -%}
{% endfor -%}
{%- endif -%}
{%- endfor -%}

