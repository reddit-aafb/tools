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
import codecs
import sys
import traceback
from pathlib import Path

from praw import Reddit
from praw.exceptions import ClientException, PRAWException
from praw.models import Subreddit

from helpers import parent_parser

MAX_EDIT_REASON_LENGTH = 256


class Deployer:
    def __init__(self, sub: Subreddit):
        self.sub = sub

    def put(self, stylesheet, images, reason):
        reason = reason[:MAX_EDIT_REASON_LENGTH]
        for name, image_path in images:
            print("Upload %s as %%%%%s%%%%" % (image_path, name))
            self.sub.stylesheet.upload(name, str(image_path))
        if stylesheet is not None:
            print("Put style\n%s\n" % stylesheet)
            self.sub.stylesheet.update(stylesheet, reason)

    def clear(self):
        self.put("", [], "Clearing stylesheet")
        for image in self.sub.stylesheet().images:
            self.sub.stylesheet.delete_image(image['name'])


class StyleSheetUpdater:

    def __init__(self):
        parser = argparse.ArgumentParser(description="Subreddit style deployer", parents=[parent_parser])
        parser.add_argument("-c", "--clear", action='store_true',
                            help="Clear subreddit styles and images before uploading (rarely necessary)")
        parser.add_argument("-n", "--no-images", action='store_true', help="Skip uploading images")
        parser.add_argument("subreddit", help="Subreddit to upload to")
        parser.add_argument("reason", help="Update comment")
        parser.add_argument("files", metavar="FILE", type=argparse.FileType('rb'), nargs='*',
                            help="Files to update from. Only one CSS file will be used. All other files will be uploaded as images")
        self.args = parser.parse_args()

        try:
            self.r = Reddit(self.args.site)
        except ClientException:
            traceback.print_exc()
            sys.stderr.write("\nOh dear, something broke. Most likely you need to pass the --site "
                             "parameter or set the praw_site environment variable\n\n")
            parser.print_help()
            sys.exit(1)

        self.deployer = Deployer(self.r.subreddit(self.args.subreddit))

    def main(self):

        if self.args.clear:
            print("Clear all images and styles")
            if not self.args.dry_run:
                self.deployer.clear()

        stylesheet = None
        images = []
        for fp in self.args.files:
            fn = Path(fp.name)
            if fn.suffix.lower() == '.css':
                print("Stylesheet: %s" % fn)
                stylesheet = codecs.getreader("UTF-8")(fp).read()
            else:
                if self.args.no_images:
                    print("Not uploading image %s" % fn)
                    continue
                images.append((fn.stem, fn))

        print("Uploading files: %r" % images)
        print("Put styles:\n%s\n" % stylesheet)
        if not self.args.dry_run:
            self.deployer.put(stylesheet, images, reason=self.args.reason)


def main():
    u = StyleSheetUpdater()
    u.main()


if __name__ == '__main__':
    main()
