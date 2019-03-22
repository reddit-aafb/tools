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

from helpers import parent_parser

MAX_EDIT_REASON_LENGTH = 256


class StyleSheetUpdater():

    def __init__(self):
        parser = argparse.ArgumentParser(description="Flair swiss army knife", parents=[parent_parser])
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

        self.subreddit = self.r.subreddit(self.args.subreddit)

    def main(self):

        if self.args.clear:
            self.clear()

        stylesheet = None
        for fp in self.args.files:
            fn = Path(fp.name)
            if fn.suffix.lower() == '.css':
                print("Stylesheet: %s" % fn)
                stylesheet = codecs.getreader("UTF-8")(fp)
            else:
                if self.args.no_images:
                    print("Not uploading image %s" % fn)
                    continue
                try:
                    self.upload_file(fn)
                    pass
                except ClientException as e:
                    print("Failed uploading %s" % fn)
                    traceback.print_exc()
        # Need to do this last, or the images wouldn't be there
        if stylesheet:
            self.put_stylesheet(stylesheet.read(), reason=self.args.reason)

    def put_stylesheet(self, styles, reason=u''):
        print(
            "Put stylesheet to %s:\n"
            "-------------------------------------------------\n"
            "%s\n"
            "-------------------------------------------------" % (self.subreddit.display_name, styles))
        try:
            reason = reason[:MAX_EDIT_REASON_LENGTH]
            if not self.args.dry_run:
                r = self.subreddit.stylesheet.update(styles, reason=reason)
                print(repr(r))
        except PRAWException as e:
            traceback.print_exc()
            raise e

    def upload_file(self, fn):
        print("upload file %s" % fn)
        if not self.args.dry_run:
            self.subreddit.stylesheet.upload(fn.stem, str(fn))

    def clear(self):
        print("clear all styles and files")
        existing_styles = self.subreddit.stylesheet()
        if not self.args.dry_run:
            self.put_stylesheet('')
        for image in existing_styles.images:
            print("  Removing %(name)s" % image)
            if not self.args.dry_run:
                self.subreddit.stylesheet.delete_image(image['name'])


def main():
    u = StyleSheetUpdater()
    u.main()


if __name__ == '__main__':
    main()
