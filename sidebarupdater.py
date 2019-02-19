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
import re

import pendulum
from praw import Reddit
from praw.models import TextArea

from aafclient import AAFClient
from helpers import RenderHelper, diff_strings
from reddittoken import ensure_scopes


def make_schedule_ctx(week, week_games, all_weeks):
    ctx = {
        'week': week,
        'games': week_games,
        'all_weeks': all_weeks,
    }
    return ctx

def make_standings_ctx(divisions):
    ctx = {
        'divisions': {}
    }
    for division, teams in divisions.items():
        ctx['divisions'][division] = []
        for team in teams:
            team.stats = team.seasons_connection.edges[0].stats
            ctx['divisions'][division].append(team)
    return ctx

def marker_replace(marker_start, marker_end, content, subject):
    replacement = "%s\n\n%s\n\n%s" % (marker_start, content, marker_end)
    return re.sub(r'(?ms)' + re.escape(marker_start) + '.*?' + re.escape(marker_end), replacement, subject)


def main():
    import sys
    sr_name = sys.argv[1]
    renderer = RenderHelper(sr_name)
    aaf = AAFClient('aaf_standings;reddit.com/r/%s' % sr_name)

    standings = aaf.standings()
    standings_ctx = make_standings_ctx(standings)
    standings = renderer.render('standings.md', standings_ctx)

    week, games = aaf.schedule(for_week=pendulum.now())
    all_weeks = aaf.schedule()
    schedule_ctx = make_schedule_ctx(week, games, all_weeks)
    schedule = renderer.render('schedule.md', schedule_ctx)

    r = Reddit('aaf_robot')
    ensure_scopes(r)

    sub = r.subreddit(sr_name)
    old_sidebar = sub.description
    new_sidebar = marker_replace('#### [](/blank "START schedule")', '#### [](/blank "END schedule")', schedule,
                                 old_sidebar)
    new_sidebar = marker_replace('#### [](/blank "START standings")', '#### [](/blank "END standings")', standings,
                                 new_sidebar)
    if old_sidebar != new_sidebar:
        print(diff_strings(old_sidebar, new_sidebar, fromfile='old_sidebar_%s' % sub.display_name, tofile='new_sidebar_%s' % sub.display_name, n=0))
        sub.mod.update(description=new_sidebar)

    for widget in sub.widgets.sidebar:
        if not isinstance(widget, TextArea) or widget.shortName not in ('Standings', 'Schedule'):
            continue
        if widget.shortName == 'Standings':
            new_text = renderer.render('standings.md', standings_ctx, widget=True)
        elif widget.shortName == 'Schedule':
            new_text = renderer.render('schedule.md', schedule_ctx, widget=True)
        if widget.text != new_text:
            widget_name = "%s_%s_widget" % (sub.display_name, widget.shortName)
            print(diff_strings(widget.text, new_text, fromfile='old_%s' % widget_name, tofile='new_%s' % widget_name, n=3))
            widget.mod.update(text=new_text)



if __name__ == '__main__':
    main()
