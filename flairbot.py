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
import sys
import traceback
from pathlib import Path
from typing import Tuple, List

from praw import Reddit
from praw.exceptions import ClientException
from praw.models import Subreddit

from helpers import RenderHelper, diff_strings, parent_parser
from redditdata import aaf_flair, nfl_flair, aaf_teams
from reddittoken import ensure_scopes

APPLICATION_SCOPES = "read,modflair,privatemessages,flair,wikiread,wikiedit,structuredstyles"


def determine_flair(aaf: str, nfl: str) -> Tuple[str, str, List[str]]:
    flair_string = []
    flair_classes = []
    flair_emojis = []

    if aaf not in aaf_flair:
        raise Exception("Unknonwn AAF flair: %s" % aaf)
    css, text, emoji = aaf_flair[aaf]
    flair_string.append(text)
    flair_classes.append(css)
    flair_emojis.append(emoji)

    if nfl and nfl in nfl_flair:
        css, text, emoji = nfl_flair[nfl]
        flair_string.append(text)
        flair_classes.append(css)
        flair_emojis.append(emoji)

    return " \u2022 ".join(flair_string), " ".join(flair_classes), flair_emojis


def create_template(sub: Subreddit, text: str, css_class: str, emojis: List[str], mod_only: bool = True) -> str:
    """
    Create a flair template that fullfills the following criteria:
    * Only shows text on old reddit (no emoji)
    * Shows emoji + Text on new reddit

    :param sub: The subreddit to work on
    :param text: (Plain) Text for the flair
    :param css_class: CSS class
    :param emojis: Emojis to add in front
    :param mod_only: Whether to make the template mod_only (Default: True)
    :return: The id of the created template
    """
    templates_before = [template['id'] for template in sub.flair.templates]
    # First we create an old-style template
    x = sub.flair.templates.add(text=text, css_class=css_class)
    new_template = list(filter(lambda t: t['id'] not in templates_before, sub.flair.templates))[0]
    # Then we update the text with the emojis in it on the new flair endpoint. This seems to be preferable.
    if emojis:
        # Prepend any emojis
        text = ":" + ("::".join(emojis)) + ": " + text
    sub.flair.templates.update(new_template['id'], mod_only=mod_only, text_editable=False,
                               background_color='transparent', text=text)
    new_template = list(filter(lambda t: t['id'] not in templates_before, sub.flair.templates))[0]
    return new_template['id']


def assignflair(r: Reddit, sub: Subreddit, dry_run: bool) -> None:
    messages = []
    for message in r.inbox.unread(limit=None):
        try:
            body = message.body
            subject = message.subject
            if not subject.startswith("Flair "):
                print("Ignoring and marking as read: %s" % subject)
                messages.append(message)
            elif subject.lower() == "flair " + sub.display_name.lower():
                m = re.match(r"^aaf:(?P<aaf>[A-Z]{2,3})( nfl:(?P<nfl>[A-Z]{2,3}))?", body.split("\n")[0])
                if m:
                    flair_str, flair_css, emojis = determine_flair(m.group('aaf'), m.group('nfl'))
                    print("Assign text=<%s>, classes=<%s>, emoji=<%r> to %s" %
                          (flair_str, flair_css, emojis, message.author))
                    if not dry_run:
                        sub.flair.set(message.author, text=":" + ("::".join(emojis)) + ": " + flair_str,
                                      css_class=flair_css)
                else:
                    print("Body <%s> from %s doesn't match" % (body, message.author))
                messages.append(message)
            else:
                print("Ignoring: %s" % subject)
        except Exception:
            traceback.print_exc()
    if not dry_run:
        r.inbox.mark_read(messages)


def updatestats(sub: Subreddit, dry_run: bool) -> None:
    stats = {}
    for f in sub.flair(limit=None):
        team = f['flair_css_class'].replace('official', '').strip()
        if team == 'aafb':
            # This is hardcoded because it doesn't belong in the teams list... grr
            team = {'subreddit': 'aafb', 'flair_class': 'aafb', 'flair_text': 'AAF', 'flair_emoji': 'AAF'}
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
        if not dry_run:
            page.edit(rdr, reason="Updated flair stats  ")


def dump(sub: Subreddit):
    import csv
    writer = csv.DictWriter(sys.stdout, ['username', 'flair_text', 'flair_css_class'], extrasaction='ignore')
    writer.writeheader()
    for user in sub.flair():
        user['username'] = user['user'].name
        writer.writerow(user)


def reset_flair(sub: Subreddit, aaf_folder: Path, nfl_folder: Path, dry_run: bool) -> None:
    print("Deleting all templates")
    if not dry_run:
        sub.flair.templates.clear()
    for emoji in sub.emoji:
        print("Delete emoji %s" % emoji)
        if not dry_run:
            emoji.delete()
    for flair_class, (flair_class, flair_text, emoji) in aaf_flair.items():
        logo = aaf_folder / (flair_text + ".png")
        print("Upload %s as :%s:" % (logo, emoji))
        print("Create template class=<%s>, text=<%s>, emojis=<%s>" % (flair_class, flair_text, emoji))
        if not dry_run:
            sub.emoji.add(emoji, str(logo))
            create_template(sub, flair_text, flair_class, [emoji], False)
    for flair_class, (flair_class, flair_text, emoji) in nfl_flair.items():
        logo = nfl_folder / (flair_text + ".png")
        print("Upload %s as :%s:" % (logo, emoji))
        if not dry_run:
            sub.emoji.add(emoji, str(logo))


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Flair swiss army knife", parents=[parent_parser])
    parser.add_argument('sr_name', help="Name of subreddit to run on")
    parser.add_argument('cmd', help="Command to run",
                        choices=[f.__name__ for f in (assignflair, updatestats, reset_flair, dump)])
    args = parser.parse_args()

    sr_name = args.sr_name
    action = args.cmd

    try:
        r = Reddit(args.site)
    except ClientException:
        traceback.print_exc()
        sys.stderr.write("\nOh dear, something broke. Most likely you need to pass the --site "
                         "parameter or set the praw_site environment variable\n\n")
        parser.print_help()
        sys.exit(1)

    ensure_scopes(r, scopes=APPLICATION_SCOPES)

    sub = r.subreddit(sr_name)

    if action == assignflair.__name__:
        assignflair(r, sub, args.dry_run)
    elif action == updatestats.__name__:
        updatestats(sub, args.dry_run)
    elif action == reset_flair.__name__:
        reset_flair(sub, Path('aaf'), Path('nfl'), args.dry_run)
    elif action == dump.__name__:
        dump(sub)


if __name__ == '__main__':
    main()
