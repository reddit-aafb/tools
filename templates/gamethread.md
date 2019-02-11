{% set home = game.home_team %}
{% set away = game.away_team %}

[{{away.name}}](/r/{{away_sr}}#away) [at](#at) [{{home.name}}](/r/{{home_sr}}#home)

----

* {{ game.stadium.name }}
* {{ game.stadium.address.locality }}, {{ game.stadium.address.administrative_area_abbreviation }}

----

{% set ot = boxscore|length > 5 %}
{% set q = game.status.quarter %}
{% set phase = game.status.phase %}

{% if game.clock.seconds %}
{% set s = game.clock.seconds %}
{% set gameclock_minutes = s / 60|int %}
{% set gameclock_seconds = s % 60 %}
{% set gameclock = "%d:%02d"|format(gameclock_minutes, gameclock_seconds) %}
{% else %}
{% set gameclock = "--:--" %}
{% endif %}

| | | | | | |{% if ot %} |{% endif %}
| :-- | :-- | :-- | :-- | :-- |  :-- |{% if ot %} :--|{% endif %}
|      |**{% if q == 1 %}{{ gameclock }}{% else %}First{% endif %}**|**{% if q == 2 %}{{ gameclock }}{% else %}Second{% endif %}**|**{% if q == 3 %}{{ gameclock }}{% else %}Third{% endif %}**|**{% if q == 4 %}{{ gameclock }}{% else %}Fourth{% endif %}**{% if ot %}|**{% if q == 5 %}{{ gameclock }}{% else %}OT{% endif %}**{% endif %}| {% if phase == 'COMPLETE' %}**Final**{% elif phase != 'PLAYING' %}**{{ phase|title }}**{% endif %} |
|**{{ away.nickname }}**| {{ box_score[1]['away'] }} | {{ box_score[2]['away'] }} | {{ box_score[3]['away'] }} | {{ box_score[4]['away'] }}{% if ot %} | {{ box_score[5]['away'] }}{% endif %} | {{ game.status.away_team_points }} |
|**{{ home.nickname }}**| {{ box_score[1]['home'] }} | {{ box_score[2]['home'] }} | {{ box_score[3]['home'] }} | {{ box_score[4]['home'] }}{% if ot %} | {{ box_score[5]['home'] }}{% endif %} | {{ game.status.home_team_points }} |

----

* General information
* 

----

| | |
| :-- | --: |
| **Coverage** | {% if lines and "Caesar's" in lines %}**Odds**{% endif %} |
| {%if game.availability %}{{ game.availability[0].short_name }}{% else %}[aaf.com](https://aaf.com/){% endif %} | {% if lines and "Caesar's" in lines %}{{ home.region_name }} {{ lines["Caesar's"].spread }} O/U {{ lines["Caesar's"].total }}{% endif %} |

{% if forecast %}
| |
|:---|
| **Weather** |
| [{{ forecast.temp_f }}°F/Wind {{ forecast.windspeed_mph }}mph/{{ forecast.symbol_name }}/{% if forecast.prec_mm > 0 %}{{ forecast.prec_mm }} mm{% else %}No{% endif %} precipitation expected](https://www.yr.no/place/{{ game.place }}#weather-{{forecast.symbol_var}} "{{ forecast.credit }}") |
{% endif %}

{% if headlines %}

----

| | |
| :-- | --: |
| **Headlines** | **Communities** |
| [{{ headlines.home[0].title }}]({{ headlines.home[0].url }}) | /r/{{home_sr}} |
{% if headlines.home[0].url != headlines.away[0].url %}
| [{{ headlines.away[0].title}}]({{ headlines.away[0].url }}) | /r/{{away_sr}} |
{% else %}
| [{{ headlines.away[1].title }}]({{ headlines.away[1].url }}) | /r/{{away_sr}} |
{% endif %}
|  |  |
{% endif %}

----

{% if performers %}

* Game Stats
* 

{% set ph=performers[0] %}
{% set pa=performers[1] %}

----

| | | | | | |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **Passing** |  | **Cmp/Att** | **Yds** | **Tds** | **Ints** |
{% for p in pa['passing'][:1] -%}
| {{ p.node.legal_name.given_name[0] }}.{{ p.node.legal_name.family_name }} | [*{{ game.away_team.abbreviation }}*](/r/{{ away_sr }}) | {{ p.stats.passes_completed }}/{{ p.stats.passes_attempted }} | {{ p.stats.passing_yards }} | {{ p.stats.passing_touchdowns }} | {{ p.stats.passes_intercepted }} |
{% endfor -%}
{% for p in ph['passing'][:1] -%}
| {{ p.node.legal_name.given_name[0] }}.{{ p.node.legal_name.family_name }} | [*{{ game.home_team.abbreviation }}*](/r/{{ home_sr }}) | {{ p.stats.passes_completed }}/{{ p.stats.passes_attempted }} | {{ p.stats.passing_yards }} | {{ p.stats.passing_touchdowns }} | {{ p.stats.passes_intercepted }} |
{% endfor -%}
| **Rushing** |  | **Car** | **Yds** | **Lng** | **Tds** |
{% for p in pa['rushing'][:1] -%}
| {{ p.node.legal_name.given_name[0] }}.{{ p.node.legal_name.family_name }} | [*{{ game.away_team.abbreviation }}*](/r/{{ away_sr }}) | {{ p.stats.rushes_attempted }} | {{ p.stats.rushing_yards }} | {{ p.stats.rushing_longest_gain }} | {{ p.stats.rushing_touchdowns }} |
{% endfor -%}
{% for p in ph['rushing'][:1] -%}
| {{ p.node.legal_name.given_name[0] }}.{{ p.node.legal_name.family_name }} | [*{{ game.home_team.abbreviation }}*](/r/{{ home_sr }}) | {{ p.stats.rushes_attempted }} | {{ p.stats.rushing_yards }} | {{ p.stats.rushing_longest_gain }} | {{ p.stats.rushing_touchdowns }} |
{% endfor -%}
| **Receiving** |  | **Rec** | **Yds** | **Lng** | **Tds** |
{% for p in pa['receiving'][:2] -%}
| {{ p.node.legal_name.given_name[0] }}.{{ p.node.legal_name.family_name }} | [*{{ game.away_team.abbreviation }}*](/r/{{ away_sr }}) | {{ p.stats.receptions }} | {{ p.stats.receiving_yards }} | {{ p.stats.receiving_longest_gain }} | {{ p.stats.receiving_touchdowns }} |
{% endfor -%}
{% for p in ph['receiving'][:2] -%}
| {{ p.node.legal_name.given_name[0] }}.{{ p.node.legal_name.family_name }} | [*{{ game.home_team.abbreviation }}*](/r/{{ home_sr }}) | {{ p.stats.receptions }} | {{ p.stats.receiving_yards }} | {{ p.stats.receiving_longest_gain }} | {{ p.stats.receiving_touchdowns }} |
{% endfor -%}


{% endif %}

{% if scoring and scoring|length > 0 %}
----

* Scoring Summary
*

----

| | | | |
| :--: | :--: | :-- | :-- |
| **Team** | **Q** | **Type** | **Drive** |
{% for drive_id, drive in scoring|dictsort %}| [*{{ drive.team.short }}*]({{ drive.team.subreddit }}) | {{ drive.qtr }} | {{ drive.type }} | {{ drive.desc }} |
{% endfor -%}

{% endif %}

----

* Thread Notes
* [Message The Moderators](http://www.reddit.com/message/compose?to=%2Fr%2Faafb)

----

| |
| :-- |
| Discuss whatever you wish. You can trash talk, but keep it civil. |
| If you are experiencing problems with comment sorting in the official reddit app, we suggest using a third-party client instead ([Android](/r/Android/comments/7ctdf4/lets_settle_this_randroid_what_is_the_best_reddit/), [iOS](/r/ios/comments/68odw1/what_is_the_best_reddit_app_for_ios/)) |
{%- if thread %}
| Turning comment sort to ['new']({{ thread.permalink }}?sort=new) will help you see the newest comments. |
{%- endif %}
| Try [Tab Auto Refresh](https://mybrowseraddon.com/tab-auto-refresh.html) to auto-refresh this tab. |
{%- if thread %}
| Use [reddit-stream.com](http://reddit-stream.com/comments/{{ thread.id }}) to get an autorefreshing version of this page |
{%- endif %}
{#-
| Check in on the r/nfl chat: **#reddit-nfl** on FreeNode ([open in browser](http://webchat.freenode.net/?channels=reddit-nfl)). |
#}
| Show your team affiliation - pick your team's logo in the sidebar. |
