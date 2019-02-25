# Schedule
{%- set ourteam='ARI' -%}
{%- set tz= 'US/Eastern' -%}
{%- set includepost=False -%}

{%- for week_id, (week, games) in all_weeks.items() if includepost or week.subseason != 'POST' -%}
    {%- if loop.changed(week.subseason) %}

## {{ week.subseason|title }} Season

| Wk | Date | Team | Time | Network |
|:--:|:-----|-----:|:----:|:-------:|
{%- endif %}
    {%- for game in games if game.home_team.abbreviation == ourteam or game.away_team.abbreviation == ourteam -%}
        {% set awaygame=game.away_team.abbreviation == ourteam -%}
        {% if game.status -%}
        {% set theirscore=game.status.home_team_points if awaygame else game.status.away_team_points -%}
        {% set ourscore=game.status.away_team_points if awaygame else game.status.home_team_points -%}
        {% if ourscore > theirscore -%}
        {% set result='W' -%}
        {% elif ourscore < theirscore -%}
        {% set result='L' -%}
        {% else -%}
        {% set result='T' -%}
        {% endif -%}
        {% endif -%}
        {% if week.subseason == 'REGULAR' -%}
            {% set week_no=week.name.replace('Week ','') -%}
        {% elif week.subseason == 'PRE' -%}
            {% set week_no=week.name.replace('Preseason Week ', '') -%}
        {% else -%}
            {% set week_no=week.name -%}
        {% endif -%}
        {% if game.status -%}
            {%- set home_points = game.status.home_team_points -%}
            {%- set away_points = game.status.away_team_points -%}
        {%- else -%}
            {%- set home_points = 0 -%}
            {%- set away_points = 0 -%}
        {%- endif %}
| {{ week_no }} | {{ game.time|format_date('ddd MMM D', tz=tz) }} | {% if awaygame %}@[*{{ game.home_team.abbreviation }}*](/r/{{ game.home_team|team_sr }}){% else %}[*{{ game.away_team.abbreviation }}*](/r/{{ game.away_team|team_sr }}){% endif %} | {% if game.status and game.status.phase == 'COMPLETE' %}**{{ result }}** | {{ game.status.home_team_points }} - {{ game.status.away_team_points }}{% else %}{{ game.time|format_date('hA', tz=tz) }} | {{ game.availability[0].short_name|short_channel }}{% endif %} |
    {%- endfor -%}
{% endfor -%}
