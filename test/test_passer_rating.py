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

from unittest import TestCase

from helpers import passer_rating


class TestPasserRating(TestCase):
    def test_passer_rating(self):
        pr = passer_rating(20, 20, 250, 5, 0)
        self.assertAlmostEqual(pr, 158.3, 1)

    def test_passer_rating_examples(self):
        examples = [
            (71.4, (35, 21, 262, 0, 1)), # Brady, Super Bowl LIII
            (57.9, (38, 19, 229, 0, 1)), # Goff, Super Bowl LIII
        ]
        for expected, (attempts, completions, yards, tds, ints) in examples:
            pr = passer_rating(attempts, completions, yards, tds, ints)
            self.assertEqual(expected, pr, "QBR For ATT=%d, CMP=%d, YDS=%d, TD=%d, INT=%d" % (attempts, completions, yards, tds, ints))
