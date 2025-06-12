import unittest
from core.mutator import Mutator

class TestMutator(unittest.TestCase):

    def setUp(self):
        self.mutator = Mutator()

    def test_repeat_letters(self):
        self.assertEqual(self.mutator.repeat_letters("test"), "tteesstt")
        self.assertEqual(self.mutator.repeat_letters("a"), "aa")
        self.assertEqual(self.mutator.repeat_letters(""), "")

    def test_leetspeak(self):
        self.assertEqual(self.mutator.leetspeak("leet"), "1337")
        self.assertEqual(self.mutator.leetspeak("hello"), "h3ll0")
        self.assertEqual(self.mutator.leetspeak(""), "")

    def test_case_variations(self):
        variations = self.mutator.case_variations("word")
        expected_variations = {"word", "Word", "wOrd", "woRd", "worD", "WORD", "wORD", "WoRD", "WOrd", "WOrD"}
        self.assertTrue(expected_variations.issubset(variations))

    def test_add_suffixes(self):
        self.assertIn("test123", self.mutator.add_suffixes("test"))
        self.assertIn("test!", self.mutator.add_suffixes("test"))
        self.assertIn("test_dev", self.mutator.add_suffixes("test"))

    def test_insert_symbols(self):
        self.assertIn("te!st", self.mutator.insert_symbols("test"))
        self.assertIn("t@est", self.mutator.insert_symbols("test"))
        self.assertIn("te#st", self.mutator.insert_symbols("test"))

if __name__ == '__main__':
    unittest.main()