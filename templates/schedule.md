# {{ week.name }}

| Time | Away |   |  @  |   | Home |
|:-----|:----:|--:|:---:|:--|:----:|
{%- for game in games %}
| {{ game.time_eastern.format('ddd h:mmA') }} | [*{{game.away_team.abbreviation}}*](/r/{{game.away_team.sr}}) | {% if game.status.phase == 'COMPLETE' and game.away_points > game.home_points %}**{{game.away_points}}**{% else %}{{game.away_points}}{% endif %} | @ | {% if game.status.phase == 'COMPLETE' and game.home_points > game.away_points %}**{{game.home_points}}**{% else %}{{game.home_points}}{% endif %} | [*{{game.home_team.abbreviation}}*](/r/{{game.home_team.sr}}) |
{%- endfor -%}
