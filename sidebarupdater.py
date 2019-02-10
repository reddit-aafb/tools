#!/usr/bin/env python

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


import pendulum

from aafclient import AAFClient
from helpers import RenderHelper
from redditdata import subreddits


def make_schedule_ctx(week, games):
    ctx = {
        'week': week,
        'games': [],
    }
    for game in games:
        game.time_eastern = pendulum.instance(game.time).in_timezone("US/Eastern")
        game.home_team.sr = subreddits[game.home_team.abbreviation]
        game.away_team.sr = subreddits[game.away_team.abbreviation]
        game.home_points = game.status.home_team_points if game.status else 0
        game.away_points = game.status.away_team_points if game.status else 0
        ctx['games'].append(game)
    return ctx


def main():
    renderer = RenderHelper()
    aaf = AAFClient('aaf_standings;reddit.com/r/aafb')
    week, games = aaf.schedule(for_week=pendulum.now())
    ctx = make_schedule_ctx(week, games)
    schedule = renderer.render('schedule.html', ctx)
    print(schedule)


if __name__ == '__main__':
    main()
