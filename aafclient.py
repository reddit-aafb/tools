#  Copyright (c) 2019 by Jonas Häggqvist
#
#  Permission to use, copy, modify, and/or distribute this software for any
#  purpose with or without fee is hereby granted, provided that the above
#  copyright notice and this permission notice appear in all copies.
#
#  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#  WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#  MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
#  SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#  WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION
#  OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
#  CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from datetime import timedelta

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from aaf_schema import aaf_schema as schema

URL = "https://api.platform.aaf.com/v1/graphql"


class AAFClient:

    def __init__(self, user_agent):
        self.endpoint = HTTPEndpoint(URL, base_headers={'User-Agent': user_agent}, timeout=15)

    def schedule(self, for_week=None):
        op = Operation(schema.Query)
        season = op.seasons_connection(last=1)
        season.nodes.named_time_ranges_connection(last=25).nodes.__fields__('id', 'name', 'time', 'subseason',
                                                                            'duration_milliseconds')
        games = season.nodes.games_connection(last=80)
        games.nodes.time()
        games.nodes.named_time_range().id()
        games.nodes.home_team().__fields__('abbreviation', 'name', 'region_name', 'nickname')
        games.nodes.away_team().__fields__('abbreviation', 'name', 'region_name', 'nickname')
        games.nodes.status().__fields__('home_team_points', 'away_team_points', 'phase')
        games.nodes.availability().short_name()
        result = self._execute(op)

        weeks = {}
        season = result.seasons_connection.nodes[0]
        for week in season.named_time_ranges_connection.nodes:
            weeks[week.id] = (week, [])
        for game in season.games_connection.nodes:
            weeks[game.named_time_range.id][1].append(game)

        if for_week is not None:
            for week_id, (week, games) in weeks.items():
                if week.time < for_week < week.time + timedelta(milliseconds=week.duration_milliseconds):
                    return week, games
        return weeks

    def game2(self, gid):
        # I'm having a bit of a struggle figuring out how to make this query using sgqlc
        query = """
{
  node(id: "Gjm5E9bwm9-ZIwVYJqIG6cvI2Ner") {
    ... on Game {
	    id,
	    time,
      homeTeamEdge {
        ...gameTeamEdge
      }
      awayTeamEdge {
        ...gameTeamEdge
      }
    }
  }
}

fragment gameTeamEdge on GameTeamEdge {
  node {
    abbreviation,
    name,
    regionName,
    nickname
  }
  stats {
    passingPlays
    rushingPlays
  }
}
"""
        return self.endpoint(query)

    def game(self, gid):
        all_game_times = self.all_game_times()
        # print(all_game_times)
        games = list(filter(lambda g: g.id == gid, all_game_times))
        if len(games) == 0:
            return None
        gametime = games[0].time

        op = Operation(schema.Query)
        games = op.games_connection(first=60, at_or_after_time=gametime, before_time=gametime + timedelta(hours=12))
        games.nodes.id()

        home_team = games.nodes.home_team()
        home_team.region_name()
        home_team.nickname()
        home_team.abbreviation()
        home_team.name()

        away_team = games.nodes.away_team()
        away_team.region_name()
        away_team.nickname()
        away_team.abbreviation()
        away_team.name()

        status = games.nodes.status()
        status.home_team_points()
        status.away_team_points()
        status.phase()
        status.quarter()

        games.nodes.stadium().__fields__('name')
        games.nodes.stadium().address().__fields__('locality', 'administrative_area_abbreviation')

        games = self._execute(op).games_connection.nodes
        return list(filter(lambda g: g.id == gid, games))[0]

    def all_game_times(self):
        op = Operation(schema.Query)
        games = op.games_connection(first=60)
        games.nodes.id()
        games.nodes.time()
        return self._execute(op).games_connection.nodes

    def _execute(self, op):
        # print(op)
        data = self.endpoint(op)
        # print(data)
        return op + data

    def games_between(self, dateafter, datebefore):
        op = Operation(schema.Query)
        games = op.games_connection(first=60, at_or_after_time=dateafter, before_time=datebefore)
        games.nodes.id()
        games.nodes.time()
        games.nodes.clock().seconds()
        games.nodes.availability().short_name()

        home_team_edge = games.nodes.home_team_edge()
        home_team_stats = home_team_edge.stats()
        home_team_stats.__fields__()
        home_team = home_team_edge.node()
        home_team.region_name()
        home_team.nickname()
        home_team.abbreviation()
        home_team.name()
        home_team.seasons_connection(last=1).edges.stats().__fields__('games_won', 'games_lost')

        away_team_edge = games.nodes.away_team_edge()
        away_team_stats = away_team_edge.stats()
        away_team_stats.__fields__()
        away_team = away_team_edge.node()
        away_team.region_name()
        away_team.nickname()
        away_team.abbreviation()
        away_team.name()
        away_team.seasons_connection(last=1).edges.stats().__fields__('games_won', 'games_lost')

        status = games.nodes.status()
        status.home_team_points()
        status.away_team_points()
        status.phase()
        status.quarter()
        status.away_team_points_by_quarter()
        status.home_team_points_by_quarter()

        players = games.nodes.players_connection(first=500)
        players.edges.team.abbreviation()
        players.edges.stats().__fields__()
        players.edges.node.legal_name().__fields__('family_name', 'given_name', 'pronunciation')

        games.nodes.stadium().__fields__('name')
        games.nodes.stadium().address().__fields__('locality', 'administrative_area_abbreviation')

        result = self._execute(op)
        if hasattr(result, 'games_connection'):
            return result.games_connection.nodes
        return []

    def standings(self):
        op = Operation(schema.Query)
        teams = op.teams_connection(first=8)
        division = teams.nodes.division()
        division.name()
        division.id()
        division.abbreviation()
        teams.nodes.abbreviation()
        teams.nodes.nickname()
        teams.nodes.region_name()
        season = teams.nodes.seasons_connection(last=1)
        standing = season.edges.standing()
        standing.__fields__()
        result = self._execute(op)

        standings = {}
        divs = {}
        for team in result.teams_connection.nodes:
            # Some hoop-jumping to use a single division object as the key and get things grouped nicely
            if team.division.id not in divs:
                divs[team.division.id] = team.division
            key = divs[team.division.id]
            if key not in standings:
                standings[key] = []
            standings[key].append(team)

        def standings_key(team):
            return team.seasons_connection.edges[0].standing.division_rank
        for div in standings:
            standings[div] = sorted(standings[div], key=standings_key)
        return standings
