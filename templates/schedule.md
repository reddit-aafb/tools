{%- set tz= 'US/Eastern' -%}
# {{ week.name }}

| Time | Away |   |  @  |   | Home | TV |
|:-----|:----:|--:|:---:|:--|:----:|:--:|
{%- for game in games %}
{% set hs = game.status.home_team_points if game.status else 0 -%}
{% set as = game.status.away_team_points if game.status else 0 -%}
| {{ game.time|format_date('ddd h:mm', tz=tz) }} | [*{{game.away_team.abbreviation}}*](/r/{{game.away_team|team_sr}}) | {% if game.status.phase == 'COMPLETE' and as > hs %}**{{as}}**{% else %}{{as}}{% endif %} | @ | {% if game.status.phase == 'COMPLETE' and hs > as %}**{{hs}}**{% else %}{{hs}}{% endif %} | [*{{game.home_team.abbreviation}}*](/r/{{game.home_team|team_sr}}) | {{ game.availability[0].short_name|short_channel }} |
{%- endfor -%}
