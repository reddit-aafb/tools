{% set ourdivision = 'West' -%}
{% set ourteam = 'ARI' -%}
{% for division, teams in divisions.items() -%}
{% if division.name == ourdivision -%}
# {{ division.name }} Standings

| Team | W | L | PCT |
|:-----|--:|--:|----:|
{% for team in teams -%}
{%- if team.stats.games_played > 0 -%}
{%- set pct=team.stats.games_won / team.stats.games_played -%}
{%- else -%}
{%- set pct=0 -%}
{%- endif -%}
{% if team.abbreviation == ourteam -%}
| [**{{ team.nickname }}**](/r/{{team|team_sr}}) | **{{ team.stats.games_won }}** | **{{ team.stats.games_lost }}** | **{{ "%0.3f"|format(pct) }}** |
{% else -%}
| [{{ team.nickname }}](/r/{{team|team_sr}}) | {{ team.stats.games_won }} | {{ team.stats.games_lost }} | {{ "%0.3f"|format(pct) }} |
{% endif -%}
{% endfor -%}
{%- endif -%}
{%- endfor -%}
