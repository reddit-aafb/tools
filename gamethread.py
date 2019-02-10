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

from datetime import timedelta

import pendulum
from fcache.cache import FileCache
from praw import Reddit
from praw.models import Submission
from recordclass import recordclass
from reddittoken import ensure_scopes

from aaf_schema import GamePhase
from aafclient import AAFClient
from helpers import RenderHelper
from redditdata import subreddits

GameThreadGame = recordclass('GameThreadGame', ['game_id', 'time', 'threads', 'archived'])

assert GamePhase.__choices__[0] == 'COMPLETE'


def now():
    return pendulum.now()


def filters(fs, seq):
    for f in fs:
        seq = filter(f, seq)
    return seq


def make_box_score(statuses):
    quarters = {
        1: {'home': 0, 'away': 0},
        2: {'home': 0, 'away': 0},
        3: {'home': 0, 'away': 0},
        4: {'home': 0, 'away': 0},
    }
    for status in statuses:
        quarters[status.quarter] = {'home': status.home_team_points, 'away': status.away_team_points}
    return quarters


def build_stats(nodes):
    key_passing = lambda p: [getattr(p, key, 0) for key in
                             ['passes_completed', 'passes_attempted', 'passing_yards', 'passing_touchdowns',
                              'passes_intercepted']]
    # print(repr(key_passing(list(nodes)[7])))
    for node in sorted(nodes, key=key_passing, reverse=True)[0:3]:
        print(node)


class GameThreadRenderer(RenderHelper):
    def render_game(self, game, template):
        #home_player_stats = build_stats(filter(lambda p: p.team.abbreviation==game.home_team.abbreviation, game.players_connection.edges))
        ctx = dict(game=game,
                   box_score=make_box_score(game.status_history_connection.nodes),
                   away_sr=subreddits[game.away_team.abbreviation],
                   home_sr=subreddits[game.home_team.abbreviation])
        title = self.try_render(template + '_title.html', ctx)
        body = self.try_render(template + '.html', ctx)
        return title, body


class AAFGameThread:
    active_buffer = timedelta(hours=8, days=40)
    gamethread_buffer = timedelta(minutes=120)

    def __init__(self, reddit_session, sr_name, teams):
        self.r = reddit_session
        self.sub = self.r.subreddit(sr_name)
        self.teams = teams.split(',')
        self.aaf = AAFClient('aafgamethread;reddit.com/r/%s' % sr_name)
        self.games = FileCache('aafgamethread_%s' % sr_name, flag='cs')
        self.renderer = GameThreadRenderer(sr_name)

    def get_games(self):
        # Get all games from aaf.com
        all_games = self.aaf.all_game_times()
        for game in all_games:
            # Put an empty one in the games cache if it's not there yet
            if game.id not in self.games:
                print("Adding game %s" % game)
                self.games[game.id] = GameThreadGame(game_id=game.id, time=game.time, threads={}, archived=False)
            # Update the time if it differs
            elif self.games[game.id].time != game.time:
                print("Updating time of %s" % game)
                update_game = self.games[game.id]
                update_game.time = game.time
                self.games[game.id] = update_game

    def active_games(self):
        games = self.aaf.games_between(now() - self.active_buffer, now() + (2 * self.gamethread_buffer))
        return list(
            filter(lambda g: g.home_team.abbreviation in self.teams or g.away_team.abbreviation in self.teams, games))

    def post_due_threads(self, active_games):
        # For each game, verify that
        for game in active_games:
            # If now > game.time-30 minutes a game thread has been posted
            gt_buffer = self.gamethread_buffer
            stored_game = self.games[game.id]
            if now() > game.time - gt_buffer and 'gamethread' not in stored_game.threads:
                print("Should have a game thread for %s" % game)
                self.submit_thread(game, 'gamethread')
            # If game.phase = COMPLETED a post game thread has been posted
            if game.status and game.status.phase == GamePhase.COMPLETE and 'post_gamethread' not in stored_game.threads:
                print("Should have a post game thread for %s" % game)
                self.submit_thread(game, 'post_gamethread')

    def submit_thread(self, game, thread_type):
        title, body = self.renderer.render_game(game, thread_type)
        if not title:
            print("ERROR: Could not render title for %s for %s" % (thread_type, game))
            return
        print("Posting to %s: %s" % (self.sub.display_name, title))
        submission = self.sub.submit(title, body)
        thread_id = submission.id
        stored_game = self.games[game.id]
        stored_game.threads[thread_type] = thread_id
        self.games[game.id] = stored_game
        return thread_id

    def update_existing(self, active_games):
        # For all active/recent games
        # Format thread
        for game in active_games:
            stored_game = self.games[game.id]
            for thread_type in ('gamethread', 'post_gamethread'):
                if thread_type in stored_game.threads:
                    # Update body
                    thread_id = stored_game.threads[thread_type]
                    thread = Submission(self.r, id=thread_id)
                    title, body = self.renderer.render_game(game, thread_type)
                    if body != thread.selftext:
                        print("Update %s (/r/%s, %s)" % (title, self.sub.display_name, thread_id))
                        thread.edit(body)

    def archive_completed(self, active_games):
        # For all unarchived games
        # If game.phase = COMPLETED and ??? > 1 hour
        # Mark game as archived
        pass

    def dump(self):
        for game in self.games.values():
            print(game)


def main():
    import sys
    import time

    r = Reddit('aaf_gamethread')
    ensure_scopes(r)

    #gt = AAFGameThread(r, 'aafb_dev', "BIR")
    gt = AAFGameThread(r, sys.argv[1], ",".join(subreddits.keys()))

    while True:
        gt.get_games()

        active_games = gt.active_games()
        gt.archive_completed(active_games)
        if len(active_games) > 0:
            gt.post_due_threads(active_games)
            gt.update_existing(active_games)
        #break
        time.sleep(60)
    # gt.dump()


if __name__ == '__main__':
    main()
