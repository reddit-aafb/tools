{%- set away=game.away_team_edge.node -%}
{%- set home=game.home_team_edge.node -%}
{{away.name}} ({{ away.seasons_connection.edges[0].stats.games_won }}-{{ away.seasons_connection.edges[0].stats.games_lost }}) @ {{home.name}} ({{ home.seasons_connection.edges[0].stats.games_won }}-{{ home.seasons_connection.edges[0].stats.games_lost }})
