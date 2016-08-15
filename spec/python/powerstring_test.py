import powerstring as p
import unittest

class powerstringTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(p.reverse("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba", "reverse has failed")

    def test_odds(self):
        self.assertEqual(p.odds("1234567890"), "13579", "odds didn't work")

    def test_evens(self):
        self.assertEqual(p.evens("1234567890"), "24680", "evens didn't work")