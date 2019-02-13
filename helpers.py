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
import traceback

from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment


class RenderHelper:
    def __init__(self, sr_name=None):
        template_dirs = ['templates/']
        if sr_name:
            template_dirs.insert(0, 'templates/%s' % sr_name)
        self.env = SandboxedEnvironment(loader=FileSystemLoader(template_dirs))

    def try_render(self, template_file, ctx):
        try:
            return self.render(template_file, ctx)
        except Exception:
            traceback.print_exc()

    def render(self, template_file, ctx):
        template = self.env.get_template(template_file)
        return template.render(**ctx)


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
