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
import difflib
import re

import pendulum
from praw import Reddit

from aafclient import AAFClient
from helpers import RenderHelper, diff_strings
from redditdata import subreddits
from reddittoken import ensure_scopes


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

def make_standings_ctx(divisions):
    ctx = {
        'divisions': {}
    }
    for division, teams in divisions.items():
        ctx['divisions'][division] = []
        for team in teams:
            team.stats = team.seasons_connection.edges[0].stats
            team.subreddit = subreddits[team.abbreviation]
            ctx['divisions'][division].append(team)
    return ctx

def marker_replace(marker_start, marker_end, content, subject):
    replacement = "%s\n\n%s\n\n%s" % (marker_start, content, marker_end)
    return re.sub(r'(?ms)' + re.escape(marker_start) + '.*?' + re.escape(marker_end), replacement, subject)


def main():
    import sys
    renderer = RenderHelper()
    aaf = AAFClient('aaf_standings;reddit.com/r/aafb')

    standings = aaf.standings()
    ctx = make_standings_ctx(standings)
    standings = renderer.render('standings.md', ctx)

    week, games = aaf.schedule(for_week=pendulum.now())
    ctx = make_schedule_ctx(week, games)
    schedule = renderer.render('schedule.md', ctx)

    r = Reddit('aaf_robot')
    ensure_scopes(r)

    sub = r.subreddit(sys.argv[1])
    old_sidebar = sub.description
    new_sidebar = marker_replace('#### [](/blank "START schedule")', '#### [](/blank "END schedule")', schedule,
                                 old_sidebar)
    new_sidebar = marker_replace('#### [](/blank "START standings")', '#### [](/blank "END standings")', standings,
                                 new_sidebar)
    if old_sidebar != new_sidebar:
        print(diff_strings(old_sidebar, new_sidebar, fromfile='old_sidebar_%s' % sub.display_name, tofile='new_sidebar_%s' % sub.display_name, n=0))
        sub.mod.update(description=new_sidebar)


if __name__ == '__main__':
    main()
