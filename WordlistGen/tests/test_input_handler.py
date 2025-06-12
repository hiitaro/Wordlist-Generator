import unittest
from core.input_handler import InputHandler

class TestInputHandler(unittest.TestCase):

    def setUp(self):
        self.input_handler = InputHandler()

    def test_parse_args(self):
        # Test command-line argument parsing
        args = self.input_handler.parse_args(['--max-length', '12', '--leet'])
        self.assertEqual(args.max_length, 12)
        self.assertTrue(args.leet)

    def test_load_config(self):
        # Test loading configuration from a file
        config = self.input_handler.load_config('test_config.json')
        self.assertIn('names', config)
        self.assertIn('hobbies', config)

if __name__ == '__main__':
    unittest.main()