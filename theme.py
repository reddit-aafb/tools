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
import sys
import traceback
from glob import glob
from pathlib import Path
from typing import Tuple, List

from git import Repo, Commit
from praw import Reddit
from praw.exceptions import ClientException

from deployer import Deployer
from helpers import parent_parser


def get_reddit(site: str, parser: argparse.ArgumentParser) -> Reddit:
    try:
        return Reddit(site)
    except ClientException:
        traceback.print_exc()
        sys.stderr.write("\nOh dear, something broke. Most likely you need to pass the --site "
                         "parameter or set the praw_site environment variable\n\n")
        parser.print_help()
        sys.exit(1)


class ThemeUpdater:

    def __init__(self):
        parser = argparse.ArgumentParser(description="Theme updater, builder and deployer", parents=[parent_parser])
        parser.add_argument('--node', help="Path containing node binary. Will be prepended to PATH")
        parser.add_argument("subreddit", help="Subreddit to deploy to")
        parser.add_argument("repo", help="Directory containing theme repo")
        self.args = parser.parse_args()
        self.r = get_reddit(self.args.site, parser)
        self.sub = self.r.subreddit(self.args.subreddit)

    def main(self):
        commits = []
        try:
            commits = self.update_repo()
        except Exception as e:
            traceback.print_exc()

        if commits:
            commits_str = "\n".join(["* {c.summary}".format(c=commit) for commit in commits])
            retcode, stdout, stderr = self.build_theme()
            if retcode > 0:
                subject = "Theme compilation failed"
                msg = """
Updated theme could not be built.

Commits:
{0}

Stdout:
{1}

Stderr:
{2}
""".format(commits_str,
                    "\n    ".join(stdout.split("\n")),
                    "\n    ".join(stderr.split("\n")))
                self.sub.message(subject, msg)

            try:
                self.upload_theme("Automatic update")
                subject = "Theme updated"
                msg = "Theme updated. Commits:\n\n{0}".format(commits_str)
                self.sub.message(subject, msg)
            except Exception as e:
                trace = traceback.format_exc()
                subject = "Theme upload failed"
                msg = "Updated theme could not be uploaded.\n\nCommits: {0}\n\nError:\n{1}".format(
                    commits_str,
                    "\n    ".join(trace.split("\n")))
                self.sub.message(subject, msg)
        else:
            print("No new changes")

    def update_repo(self) -> List[Commit]:
        repo = Repo(self.args.repo)
        start_commit = repo.head.commit
        print("Currently on %s" % repo.active_branch.name)
        print("Currently at %s" % repo.head.commit.hexsha)
        origin = list(filter(lambda r: r.name == 'origin', repo.remotes))[0]
        origin.pull()
        print("Pulled!")
        print("Now at %s" % repo.head.commit.hexsha)
        commit = repo.head.commit
        commits = []
        while commit:
            if commit == start_commit:
                break
            commits.append(commit)
            commit = commit.parents[0] if commit.parents else None
        return commits

    def build_theme(self) -> Tuple[int, str, str]:
        cmd = [self.args.repo + "/node_modules/.bin/gulp", 'build']
        import subprocess
        import os
        my_env = os.environ.copy()
        if self.args.node:
            my_env["PATH"] = self.args.node + ":" + my_env["PATH"]
        proc = subprocess.Popen(cmd, cwd=self.args.repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding="UTF-8", env=my_env)

        stdout, stderr = proc.communicate()
        print("Built theme: %d" % proc.returncode)
        print("Stdout: %s" % stdout)
        print("Stderr: %s" % stderr)
        return proc.returncode, stdout, stderr

    def upload_theme(self, reason: str):
        d = Deployer(self.sub)
        stylesheet = open(self.args.repo + "/dist/assets/css/screen.css").read()
        images = []
        for suffix in ('png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG'):
            pattern = self.args.repo + "/dist/assets/*/*" + suffix
            images += [(Path(p).stem, p) for p in glob(pattern)]
        d.put(stylesheet, images, reason)


if __name__ == '__main__':
    t = ThemeUpdater()
    t.main()
