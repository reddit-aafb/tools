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
import argparse
import re
import sys
import traceback
from pathlib import Path
from typing import Tuple, List, TextIO, Dict

from praw import Reddit
from praw.exceptions import ClientException
from praw.models import Subreddit, WikiPage
from prawcore import NotFound

from helpers import RenderHelper, diff_strings, parent_parser, dir_path_type, yaml_file_type
from redditdata import aaf_teams
from reddittoken import ensure_scopes

APPLICATION_SCOPES = "read,modflair,privatemessages,flair,wikiread,wikiedit,structuredstyles"


def determine_flair(body: str, flairconfig: Dict) -> Tuple[str, str]:
    m = re.match(r"^primary:(?P<primary_group>[^-]+)-(?P<primary_abbr>[^ ]+)( secondary:(?P<secondary_group>[^-]+)-(?P<secondary_abbr>[^ ]+))?", body.split("\n")[0])
    if not m:
        return None

    flair_string = []
    flair_classes = []
    flair_emojis = []

    if m['primary_group'] not in flairconfig['primary'] or m['primary_abbr'] not in flairconfig['primary'][m['primary_group']]:
        raise Exception("Unknonwn Primary flair: %s-%s" % (m['primary_group'], m['primary_abbr']))
    primary_flair = flairconfig.get('primary').get(m['primary_group']).get(m['primary_abbr'])
    flair_string.append(primary_flair['text'])
    flair_classes.append(primary_flair['class'])
    flair_emojis.append(primary_flair['emoji'])

    if m['secondary_group'] is not None and m['secondary_group'] in flairconfig['secondary'] and m['secondary_abbr'] in flairconfig['secondary'][m['secondary_group']]:
        secondary_flair = flairconfig.get('secondary').get(m['secondary_group']).get(m['secondary_abbr'])
        flair_string.append(secondary_flair['text'])
        flair_classes.append(secondary_flair['class'])
        flair_emojis.append(secondary_flair['emoji'])

    return ":%s: %s" % ("::".join(flair_emojis), " \u2022 ".join(flair_string)), " ".join(flair_classes)


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


def assignflair(r: Reddit, sub: Subreddit, dry_run: bool, flairconfig: Dict) -> None:
    messages = []
    for message in r.inbox.unread(limit=None):
        try:
            body = message.body
            subject = message.subject
            subject_start = "request flair /r/"
            if subject.lower() == subject_start + sub.display_name.lower():
                result = determine_flair(body, flairconfig)
                if result is not None:
                    flair_str, flair_css = result
                    print("Assign text=<%s>, classes=<%s> to %s" %
                          (flair_str, flair_css, message.author))
                    if not dry_run:
                        sub.flair.set(message.author, text=flair_str, css_class=flair_css)
                else:
                    print("Body <%s> from %s doesn't match" % (body, message.author))
                messages.append(message)
            else:
                print("Ignoring: %s" % subject)
        except Exception:
            traceback.print_exc()
    if not dry_run:
        r.inbox.mark_read(messages)


def find_flair(param: str, flair_config: Dict):
    classes = param.split(" ")
    for group, teams in flair_config.items():
        for abbr, team in teams.items():
            if team['class'] in classes:
                return tuple([group, abbr] + list(team.values()))


def updatestats(sub: Subreddit, flair_config: Dict, dry_run: bool) -> None:
    stats = {}
    for f in sub.flair(limit=None):
        classes = f['flair_css_class'].lower().strip() if f['flair_css_class'] else None
        if not classes:
            continue
        primary = find_flair(classes, flair_config['primary'])
        secondary = find_flair(classes, flair_config['secondary'])

        if primary is None:
            continue

        if primary not in stats:
            stats[primary] = {'_total': 0}
        stats[primary]['_total'] += 1

        if secondary is not None:
            if secondary not in stats[primary]:
                stats[primary][secondary] = 0
            stats[primary][secondary] += 1

    renderer = RenderHelper(sub.display_name)
    rdr = renderer.render('flair_stats.md', {'stats': stats})

    page = sub.wiki['/flair/stats']

    update_or_create(sub, page, rdr, dry_run, edit_reason="Updated flair stats")


def dump(sub: Subreddit, outfile: TextIO):
    import csv
    writer = csv.DictWriter(outfile, ['username', 'flair_text', 'flair_css_class'], extrasaction='ignore')
    writer.writeheader()
    for user in sub.flair():
        user['username'] = user['user'].name
        writer.writerow(user)


def reset_flair(sub: Subreddit, flairconfig: Dict, emoji_dir: Path, dry_run: bool) -> None:
    print("Deleting all templates")
    if not dry_run:
        sub.flair.templates.clear()
    for emoji in sub.emoji:
        print("Delete emoji %s" % emoji)
        if not dry_run:
            emoji.delete()

    for section, groups in flairconfig.items():
        for group in groups.values():
            for flair in group.values():
                emoji_file = emoji_dir / (flair['emoji'] + ".png")
                if not emoji_file.exists():
                    raise Exception("File does not exist: %s" % emoji_file)
                print("Upload %s as :%s:" % (emoji_file, flair['emoji']))
                if not dry_run:
                    sub.emoji.add(flair['emoji'], str(emoji_file))
                if section == 'primary':
                    print("Create template class=<{class}>, text=<{text}>, emojis=<{emoji}>".format(**flair))
                    if not dry_run:
                        create_template(sub, flair['text'], flair['class'], [flair['emoji']], False)


def update_or_create(sub: Subreddit, page: WikiPage, new_content: str, dry_run, edit_reason='Automatic update'):
    try:
        if new_content != page.content_md:
            print(diff_strings(page.content_md, new_content))
            if not dry_run:
                page.edit(new_content, reason=edit_reason)
    except NotFound:
        name = page.name
        while name.startswith('/'):
            name = name[1:]
        print(diff_strings("", new_content))
        if not dry_run:
            sub.wiki.create(name, new_content, reason=edit_reason)


def wikipages(sub: Subreddit, flairconfig: Dict, wikiroot: str, dry_run: bool):
    renderer = RenderHelper(sub.display_name)
    root = sub.wiki[wikiroot]

    index = renderer.render('flairindex.md', {'flair': flairconfig['primary'], 'sub': sub, 'page': root})
    update_or_create(sub, root, index, dry_run)
    if index != root.content_md:
        print(diff_strings(root.content_md, index, n=3))
    for primary, groups in flairconfig['primary'].items():
        for abbr, primaryflair in groups.items():
            path = "%s/%s" % (wikiroot, primaryflair['text'].lower())
            page = sub.wiki[path]
            content = renderer.render('flairpage.md', {'abbr': abbr, 'primary': primaryflair, 'secondary': flairconfig['secondary'], 'sub': sub, 'page': page})
            update_or_create(sub, page, content, dry_run)


def repair_flair(sub: Subreddit, flair_config: Dict, dry_run: bool):
    valid_emojis = [emoji.name for emoji in sub.emoji]

    for f in sub.flair(limit=None):
        classes = f['flair_css_class'].lower().strip() if f['flair_css_class'] else None
        if classes == 'aafb':
            # Hardcoded mistake here
            print("Replace %r with text=<:AAF: AAF>, class=<aaf>" % f)
            if not dry_run:
                sub.flair.set(f['user'], text=":AAF: AAF", css_class="aaf")
            continue
        if not classes or 'official' in classes or 'ranker' in classes:
            print("Not touching %r" % f)
            continue
        primary = find_flair(classes, flair_config['primary'])
        secondary = find_flair(classes, flair_config['secondary'])
        if not primary:
            print("Couldn't find primary for %r" % f)
            continue
        if len(classes.split(" ")) == 2 and secondary is None:
            print("Two classes but couldn't find secondary for %r" % f)
            continue
        if len(classes.split(" ")) > 2:
            print("More than two classes for %r" % f)
            continue

        flair_emojis = re.findall(":([^:]+):", f['flair_text'])
        msg = "primary:%s-%s" % (primary[0], primary[1])
        if secondary:
            msg += " secondary:%s-%s" % (secondary[0], secondary[1])
        real_text, real_class = determine_flair(msg, flair_config)
        if not flair_emojis:
            print("%r is missing emoji" % f)
            print("Replace %r with text=<%s>, class=<%s>" % (f, real_text, real_class))
            if not dry_run:
                sub.flair.set(f['user'], text=real_text, css_class=real_class)
            continue
        for flair_emoji in flair_emojis:
            if flair_emoji not in valid_emojis:
                print("%r has invalid emoji %s" % (f, flair_emoji))
                print("Replace %r with text=<%s>, class=<%s>" % (f, real_text, real_class))
                if not dry_run:
                    sub.flair.set(f['user'], text=real_text, css_class=real_class)
                continue


def main():
    parser = argparse.ArgumentParser(description="Flair swiss army knife", parents=[parent_parser])
    parser.add_argument('sr_name', help="Name of subreddit to run on")
    parser.add_argument('flairconfig', help='Config file detailing primary and secondary flair', type=yaml_file_type)

    sp = parser.add_subparsers(help="Sub-command help", dest='cmd')
    sp.add_parser(repair_flair.__name__, help="Repair flair for users with broken flair")

    sp.add_parser(assignflair.__name__, help="Assign flair according to inbox",
                  description='Read inbox and assign flair to users')
    sp.add_parser(updatestats.__name__, help="Update stats and post to wiki")
    x = sp.add_parser(reset_flair.__name__, help="Reset flair templates for primary flair and upload emoji.",
                      description="All flair templates will be removed and created for primary flair.")
    x.add_argument('emojidir', type=dir_path_type(), help="Directory containing emoji images")

    x = sp.add_parser(dump.__name__, help="Dump subreddit flair")
    x.add_argument('outfile', nargs='?', type=argparse.FileType('w', encoding="UTF-8"), default=sys.stdout)

    x = sp.add_parser(wikipages.__name__, help="Create/update flair selector wikipages")
    x.add_argument('wikiroot')

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
        assignflair(r, sub, args.dry_run, args.flairconfig)
    elif action == updatestats.__name__:
        updatestats(sub, args.flairconfig, args.dry_run)
    elif action == reset_flair.__name__:
        reset_flair(sub, args.flairconfig, args.emojidir, args.dry_run)
    elif action == dump.__name__:
        dump(sub, args.outfile)
    elif action == wikipages.__name__:
        wikipages(sub, args.flairconfig, args.wikiroot, args.dry_run)
    elif action == repair_flair.__name__:
        repair_flair(sub, args.flairconfig, args.dry_run)


if __name__ == '__main__':
    main()
