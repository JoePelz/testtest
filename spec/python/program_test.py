import program as p
import unittest

class programTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(p.add(99, 1), 100, "program.add failed")

    def test_div(self):
        self.assertAlmostEqual(p.div(15, 7), 2.14, 2, "program.div failed")

    def test_mult(self):
        self.assertEqual(p.mult(12, 10), 120, "program.mult failed")

    def test_sub(self):
        self.assertEqual(p.sub(99, 50), 49, "program.sub failed")

