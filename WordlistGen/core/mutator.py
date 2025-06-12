class Mutator:
    def repeat_letters(self, word):
        return ''.join([char * 2 for char in word])

    def leetspeak(self, word):
        leet_dict = {
            'a': '4', 'b': '8', 'e': '3', 'g': '9', 'i': '1',
            'o': '0', 's': '5', 't': '7', 'l': '1'
        }
        return ''.join([leet_dict.get(char, char) for char in word])

    def case_variations(self, word):
        variations = set()
        for i in range(1 << len(word)):
            variation = ''.join([char.upper() if i & (1 << j) else char.lower() for j, char in enumerate(word)])
            variations.add(variation)
        return list(variations)

    def add_suffixes(self, word):
        suffixes = ['123', '!', '_dev', '2023']
        return [word + suffix for suffix in suffixes]

    def insert_symbols(self, word):
        symbols = ['@', '#', '$', '%', '^', '&']
        return [word[:i] + symbol + word[i:] for i in range(len(word) + 1) for symbol in symbols]