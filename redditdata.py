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

aaf_teams = {
    'SD': {
        'subreddit': 'SDFleet',
        'flair_class': 'Fleet',
        'flair_text': 'Fleet',
    },
    'SA': {
        'subreddit': 'CommandersSA',
        'flair_class': 'Commanders',
        'flair_text': 'Commanders',
    },
    'ATL': {
        'subreddit': 'ATLLegends',
        'flair_class': 'Legends',
        'flair_text': 'Legends',
    },
    'ORL': {
        'subreddit': 'OrlApollos',
        'flair_class': 'Apollos',
        'flair_text': 'Apollos',
    },
    'MEM': {
        'subreddit': 'MemExpress',
        'flair_class': 'Express',
        'flair_text': 'Express',
    },
    'BIR': {
        'subreddit': 'BHIron',
        'flair_class': 'Iron',
        'flair_text': 'Iron',
    },
    'SL': {
        'subreddit': 'SLCStallions',
        'flair_class': 'Stallions',
        'flair_text': 'Stallions',
    },
    'ARI': {
        'subreddit': 'ARZHotshots',
        'flair_class': 'Hotshots',
        'flair_text': 'Hotshots',
    },
}

nfl_teams = {
    'ARI': {
        'flair_class': 'nfl-cardinals',
        'flair_text': 'Cardinals',
    },
}

subreddits = {key: v['subreddit'] for key, v in aaf_teams.items()}
aaf_flair = {key: (t['flair_class'], t['flair_text']) for key, t in aaf_teams.items()}
nfl_flair = {key: (t['flair_class'], t['flair_text']) for key, t in nfl_teams.items()}
aaf_flair['AAF'] = ('aaf', 'AAF')
