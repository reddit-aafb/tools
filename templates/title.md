{%- set away=game.away_team -%}
{%- set home=game.home_team -%}
{{away.name}} ({{ away.seasons_connection.edges[0].stats.games_won }}-{{ away.seasons_connection.edges[0].stats.games_lost }}) @ {{home.name}} ({{ home.seasons_connection.edges[0].stats.games_won }}-{{ home.seasons_connection.edges[0].stats.games_lost }})
