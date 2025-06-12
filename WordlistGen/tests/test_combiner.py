import unittest
from core.combiner import Combiner

class TestCombiner(unittest.TestCase):

    def setUp(self):
        self.combiner = Combiner()

    def test_combine_templates(self):
        data = ['user1', 'user2']
        templates = ['{username}_2023', '{username}!']
        expected_output = ['user1_2023', 'user1!', 'user2_2023', 'user2!']
        result = self.combiner.combine_templates(data, templates)
        self.assertEqual(result, expected_output)

    def test_generate_variations(self):
        word = 'test'
        templates = ['{word}123', '{word}!', '{word}_dev']
        expected_output = ['test123', 'test!', 'test_dev']
        result = self.combiner.generate_variations(word)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()