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
import traceback
from typing import Tuple

import pendulum
from praw import Reddit
from praw.models import Subreddit

from helpers import RenderHelper, diff_strings
from redditdata import aaf_flair, nfl_flair, aaf_teams
from reddittoken import ensure_scopes


def determine_flair(aaf: str, nfl: str) -> Tuple[str, str]:
    flair_string = []
    flair_classes = []

    if aaf not in aaf_flair:
        raise Exception("Unknonwn AAF flair: %s" % aaf)
    css, text = aaf_flair[aaf]
    flair_string.append(text)
    flair_classes.append(css)

    if nfl and nfl in nfl_flair:
        css, text = nfl_flair[nfl]
        flair_string.append(text)
        flair_classes.append(css)

    return " / ".join(flair_string), " ".join(flair_classes)


def assignflair(r: Reddit, sub: Subreddit) -> None:
    messages = []
    for message in r.inbox.unread(limit=None):
        try:
            body = message.body
            subject = message.subject
            if not subject.startswith("Flair "):
                print("Ignoring and marking as read: %s" % subject)
                messages.append(message)
            elif subject == "Flair " + sub.display_name:
                m = re.match(r"^aaf:(?P<aaf>[A-Z]{2,3})( nfl:(?P<nfl>[A-Z]{2,3}))?", body.split("\n")[0])
                if m:
                    flair_str, flair_css = determine_flair(m.group('aaf'), m.group('nfl'))
                    print("Assign text=<%s>, classes=<%s> to %s" % (flair_str, flair_css, message.author))
                else:
                    print("Body <%s> from %s doesn't match" % (body, message.author))
                messages.append(message)
            else:
                print("Ignoring: %s" % subject)
        except Exception:
            traceback.print_exc()
    r.inbox.mark_read(messages)


def updatestats(sub: Subreddit) -> None:
    stats = {}
    for f in sub.flair(limit=None):
        team = f['flair_css_class'].replace('official', '').strip()
        if team == 'aafb':
            # This is hardcoded because it doesn't belong in the teams list... grr
            team = {'subreddit': 'aafb', 'flair_class': 'aafb', 'flair_text': 'AAF'}
        else:
            team = list(filter(lambda v: v[1]['flair_class'] == team, aaf_teams.items()))
            team = team[0][1] if len(team) > 0 else None
        if team is None:
            continue
        team = tuple(team.values())
        if team not in stats:
            stats[team] = 0
        stats[team] += 1

    renderer = RenderHelper(sub.display_name)
    rdr = renderer.render('flair_stats.md', {'stats': stats})

    page = sub.wiki['/flair/stats']

    if page.content_md != rdr:
        print("Updating page")
        print(diff_strings(page.content_md, rdr))
        page.edit(rdr, reason="Updated flair stats  ")


def main():
    import sys
    sr_name = sys.argv[1]
    action = sys.argv[2]

    r = Reddit('aaf_robot')
    ensure_scopes(r)

    # r.inbox.message('fdvvse').mark_unread()
    r.inbox.message('fdx6vp').mark_unread()
    # r.inbox.message('fdxnek').mark_unread()

    sub = r.subreddit(sr_name)

    if action == 'assignflair':
        assignflair(r, sub)
    elif action == 'updatestats':
        updatestats(sub)


if __name__ == '__main__':
    main()
