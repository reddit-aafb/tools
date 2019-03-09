{% set home = game.home_team %}
{% set away = game.away_team %}

[{{away.name}}](/r/{{away|team_sr}}#away) [at](#at) [{{home.name}}](/r/{{home|team_sr}}#home)

----

* {{ game.stadium.name }}
* {{ game.stadium.address.locality }}, {{ game.stadium.address.administrative_area_abbreviation }}

----

{% set ot = game.status.home_team_points_by_quarter|length > 4 %}
{% set q = game.status.quarter %}
{% set phase = game.status.phase if game.status and game.status.phase else 'PREGAME' %}
{% if game.status and game.status.home_team_points_by_quarter %}
{% set home_quarters = game.status.home_team_points_by_quarter %}
{% set away_quarters = game.status.away_team_points_by_quarter %}
{% else %}
{% set home_quarters = ('','','','') %}
{% set away_quarters = ('','','','') %}
{% endif %}
{% if game.clock.seconds %}
{% set s = game.clock.seconds %}
{% set gameclock_minutes = s / 60|int %}
{% set gameclock_seconds = s % 60 %}
{% set gameclock = "%d:%02d"|format(gameclock_minutes, gameclock_seconds) %}
{% else %}
{% set gameclock = "--:--" %}
{% endif %}
{% set early_game=game.time|format_date('H', tz='US/Eastern')|int < 20 -%}
[](/# "GT-TIMESLOT-{% if early_game %}EARLY{% else %}LATE{% endif %}")
[](/# "GT-PHASE-{{ phase|lower }}")

{% if phase == 'PREGAME' %}
----

* First snap
* 

| | | | | |
|:--|:--|:--|:--|:--|
| **{{ game.time|format_date('zz', tz='US/Eastern') }}** | **{{ game.time|format_date('zz', tz='US/Central') }}** | **{{ game.time|format_date('zz', tz='US/Mountain') }}** | **{{ game.time|format_date('zz', tz='US/Pacific') }}** | **{{ game.time|format_date('zz', tz='UTC') }}** |
| {{ game.time|format_date('h:mmA', tz='US/Eastern') }} | {{ game.time|format_date('h:mmA', tz='US/Central') }} | {{ game.time|format_date('h:mmA', tz='US/Mountain') }} | {{ game.time|format_date('h:mmA', tz='US/Pacific') }} | {{ game.time|format_date('h:mmA', tz='UTC') }} |

{% if gameclock != "--:--" %}Countdown to first snap: `{{ gameclock }}`{% endif %}

{% else %}
| | | | | | |{% if ot %} |{% endif %}
| :-- | :-- | :-- | :-- | :-- |  :-- |{% if ot %} :--|{% endif %}
|      |**{% if q == 1 %}{{ gameclock }}{% else %}First{% endif %}**|**{% if q == 2 %}{{ gameclock }}{% else %}Second{% endif %}**|**{% if q == 3 %}{{ gameclock }}{% else %}Third{% endif %}**|**{% if q == 4 %}{{ gameclock }}{% else %}Fourth{% endif %}**{% if ot %}|**{% if q == 5 %}{{ gameclock }}{% else %}OT{% endif %}**{% endif %}| {% if phase == 'COMPLETE' %}**Final**{% elif phase != 'PLAYING' %}**{{ phase|title }}**{% endif %} |
|**{{ away.nickname }}**| {{ away_quarters[0] }} | {{ away_quarters[1] }} | {{ away_quarters[2] }} | {{ away_quarters[3] }}{% if ot %} | {{ away_quarters[4] }}{% endif %} | {{ game.status.away_team_points }} |
|**{{ home.nickname }}**| {{ home_quarters[0] }} | {{ home_quarters[1] }} | {{ home_quarters[2] }} | {{ home_quarters[3] }}{% if ot %} | {{ home_quarters[4] }}{% endif %} | {{ game.status.home_team_points }} |
{% endif %}

----

* General information
* {% if phase == 'COMPLETE' %}[Boxscore](https://noextrapoints.com/boxscores/{{ game.id }}){% endif %}

----

| | |
| :-- | --: |
| **Coverage** | {% if lines and "Caesar's" in lines %}**Odds**{% endif %} |
| {%if game.availability %}{{ game.availability[0].short_name }} - {% endif %} [aaf.com](https://aaf.com/live/{{ game.id }}) | {% if lines and "Caesar's" in lines %}{{ home.region_name }} {{ lines["Caesar's"].spread }} O/U {{ lines["Caesar's"].total }}{% endif %} |

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
| [{{ headlines.home[0].title }}]({{ headlines.home[0].url }}) | /r/{{home|team_sr}} |
{% if headlines.home[0].url != headlines.away[0].url %}
| [{{ headlines.away[0].title}}]({{ headlines.away[0].url }}) | /r/{{away|team_sr}} |
{% else %}
| [{{ headlines.away[1].title }}]({{ headlines.away[1].url }}) | /r/{{away|team_sr}} |
{% endif %}
|  |  |
{% endif %}

----

{% if performers and game.status and game.status.phase != 'PREGAME' %}

* Game Stats
* 

{% set ph=performers[0] %}
{% set pa=performers[1] %}

----

{% macro player_name(p) -%}
{% if p.node.legal_name.pronunciation %}[{{ p.node.legal_name.given_name[0] }}.{{ p.node.legal_name.family_name }}](//# "{{ p.node.legal_name.pronunciation }}"){% else %}{{ p.node.legal_name.given_name[0] }}.{{ p.node.legal_name.family_name }}{% endif %}
{%- endmacro -%}

{% if phase == 'COMPLETE' -%}
{%set passers=2 -%}
{%set rushers=2 -%}
{%set receivers=3 -%}
{% else %}
{%set passers=1 -%}
{%set rushers=1 -%}
{%set receivers=2 -%}
{% endif %}

| | | | | | |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **Passing** |  | **Cmp/Att** | **Yds** | **Tds** | **Ints** |
{% for p in pa['passing'][:passers] -%}
| {{ player_name(p) }} | [*{{ game.away_team.abbreviation }}*](/r/{{ away|team_sr }}) | {{ p.stats.passes_completed }}/{{ p.stats.passes_attempted }} | {{ p.stats.passing_yards }} | {{ p.stats.passing_touchdowns }} | {{ p.stats.passes_intercepted }} |
{% endfor -%}
{% for p in ph['passing'][:passers] -%}
| {{ player_name(p) }} | [*{{ game.home_team.abbreviation }}*](/r/{{ home|team_sr }}) | {{ p.stats.passes_completed }}/{{ p.stats.passes_attempted }} | {{ p.stats.passing_yards }} | {{ p.stats.passing_touchdowns }} | {{ p.stats.passes_intercepted }} |
{% endfor -%}
| **Rushing** |  | **Car** | **Yds** | **Lng** | **Tds** |
{% for p in pa['rushing'][:rushers] -%}
| {{ player_name(p) }} | [*{{ game.away_team.abbreviation }}*](/r/{{ away|team_sr }}) | {{ p.stats.rushes_attempted }} | {{ p.stats.rushing_yards }} | {{ p.stats.rushing_longest_gain }} | {{ p.stats.rushing_touchdowns }} |
{% endfor -%}
{% for p in ph['rushing'][:rushers] -%}
| {{ player_name(p) }} | [*{{ game.home_team.abbreviation }}*](/r/{{ home|team_sr }}) | {{ p.stats.rushes_attempted }} | {{ p.stats.rushing_yards }} | {{ p.stats.rushing_longest_gain }} | {{ p.stats.rushing_touchdowns }} |
{% endfor -%}
| **Receiving** |  | **Rec** | **Yds** | **Lng** | **Tds** |
{% for p in pa['receiving'][:receivers] -%}
| {{ player_name(p) }} | [*{{ game.away_team.abbreviation }}*](/r/{{ away|team_sr }}) | {{ p.stats.receptions }} | {{ p.stats.receiving_yards }} | {{ p.stats.receiving_longest_gain }} | {{ p.stats.receiving_touchdowns }} |
{% endfor -%}
{% for p in ph['receiving'][:receivers] -%}
| {{ player_name(p) }} | [*{{ game.home_team.abbreviation }}*](/r/{{ home|team_sr }}) | {{ p.stats.receptions }} | {{ p.stats.receiving_yards }} | {{ p.stats.receiving_longest_gain }} | {{ p.stats.receiving_touchdowns }} |
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
| Check out our game coverage on [@redditAAF](https://twitter.com/redditaaf) |
{%- if thread %}
| Turning comment sort to ['new']({{ thread.permalink }}?sort=new) will help you see the newest comments. |
{%- endif %}
| Try [Tab Auto Refresh](https://mybrowseraddon.com/tab-auto-refresh.html) to auto-refresh this tab. |
{%- if thread %}
| Use [reddit-stream.com](http://reddit-stream.com/comments/{{ thread.id }}) to get an autorefreshing version of this page |
{%- endif %}
| Check in on the r/aafb chat: **##reddit-aaf** on FreeNode ([open in browser](http://webchat.freenode.net/?channels=%23%23reddit-aaf)). |
| Show your team affiliation - pick your team's logo in the sidebar. |
