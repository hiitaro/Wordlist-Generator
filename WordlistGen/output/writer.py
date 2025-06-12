class Writer:
    def write_to_file(self, wordlist, filename):
        with open(filename, 'w') as f:
            for word in wordlist:
                f.write(f"{word}\n")

    def remove_duplicates(self, wordlist):
        return list(set(wordlist))