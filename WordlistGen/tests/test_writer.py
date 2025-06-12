import unittest
from output.writer import Writer

class TestWriter(unittest.TestCase):

    def setUp(self):
        self.writer = Writer()
        self.wordlist = ['daniil123', 'd4n11l!', 'Daniil_dev', 'daaniil@', 'petname2023', 'hobbyname123!']

    def test_write_to_file(self):
        filename = 'test_output.txt'
        self.writer.write_to_file(self.wordlist, filename)
        with open(filename, 'r') as f:
            content = f.read().splitlines()
        self.assertEqual(content, self.wordlist)

    def test_remove_duplicates(self):
        wordlist_with_duplicates = ['daniil123', 'daniil123', 'Daniil_dev', 'Daniil_dev']
        unique_wordlist = self.writer.remove_duplicates(wordlist_with_duplicates)
        self.assertEqual(unique_wordlist, ['daniil123', 'Daniil_dev'])

if __name__ == '__main__':
    unittest.main()