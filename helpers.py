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
import difflib
import os
import traceback
from pathlib import Path

import pendulum
import yaml
from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment

from redditdata import subreddits


class RenderHelper:
    def __init__(self, sr_name: str = None, base_dir: Path = None) -> None:
        if base_dir is None:
            base_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        template_dirs = [str(base_dir / 'templates/')]
        if sr_name:
            template_dirs.insert(0, str(base_dir / 'templates' / sr_name.lower()))
        self.env = SandboxedEnvironment(loader=FileSystemLoader(template_dirs))
        self.load_filters()

    def try_render(self, template_file, ctx):
        try:
            return self.render(template_file, ctx)
        except Exception:
            traceback.print_exc()

    def render(self, template_file, ctx, **kwargs):
        ctx.update(kwargs)
        template = self.env.get_template(template_file)
        return template.render(**ctx)

    def load_filters(self):
        self.env.filters['team_sr'] = team_sr
        self.env.filters['format_date'] = format_date
        self.env.filters['short_channel'] = short_channel
        self.env.filters['passer_rating'] = pr_filter


def team_sr(team):
    if team in subreddits:
        return subreddits[team]
    if hasattr(team, 'abbreviation'):
        return team_sr(team.abbreviation)
    return 'aafb'


def format_date(datetime, format, tz='US/Eastern'):
    return pendulum.instance(datetime).in_timezone(tz).format(format)


def short_channel(channel):
    channels = {
        'NFL Network': 'NFLN',
        'CBS Sports Network': 'CBS SN',
        'B/R Live': 'B/R',
        'TNT': 'TNT',
    }
    return channels.get(channel, channel)

def pr_filter(s):
    if hasattr(s, "stats"):
        return pr_filter(s.stats)
    return passer_rating(s.passes_attempted, s.passes_completed, s.passing_yards, s.passing_touchdowns, s.passes_intercepted)


def diff_strings(a, b, **kwargs):
    opts = {'fromfile': 'from', 'tofile': 'to'}
    opts.update(kwargs)
    return "\n".join(difflib.unified_diff(a.split("\n"), b.split("\n"), lineterm='', **opts))


def passer_rating(attempts: int, completions: int, yards: int, tds: int, ints: int) -> float:
    def clamp(v):
        return max(min(v, 2.375), 0.0)

    a = clamp(5 * ((completions / attempts) - 0.3))
    b = clamp(0.25 * ((yards / attempts) - 3))
    c = clamp(20 * (tds / attempts))
    d = clamp(2.375 - ((ints / attempts) * 25))

    return round(((a + b + c + d) / 6) * 100, 1)


def dir_path_type(must_exist=True, create=False, mode=0o777):
    def f(path):
        p = Path(path)
        if not p.is_dir():
            if must_exist:
                raise argparse.ArgumentError("Path %s does not exist" % path)
            elif create:
                try:
                    p.mkdir(parents=True, mode=mode)
                except Exception as e:
                    raise argparse.ArgumentError("Could not create path %s" % path) from e
        return p
    return f


def yaml_file_type(filename):
    with open(filename) as fp:
        return yaml.load(fp, loader=yaml.SafeLoader)


parent_parser = argparse.ArgumentParser('Subreddit flair swiss army knife', add_help=False)
parent_parser.add_argument('--site', help="Reddit 'site' (praw.ini section) to use")
parent_parser.add_argument('--dry-run', action="store_true", help="Prevent any action on reddit being taken "
                                                                  "(other side-effects are not prevented!)")
