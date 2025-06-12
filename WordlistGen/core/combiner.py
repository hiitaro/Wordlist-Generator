class Combiner:
    def combine_templates(self, data, templates):
        combined_words = []
        for template in templates:
            for item in data:
                combined_words.append(template.replace("{word}", item))
        return combined_words

    def generate_variations(self, word):
        variations = []
        # Example variations could be added here
        variations.append(word)
        variations.append(word.upper())
        variations.append(word.lower())
        variations.append(word[::-1])  # Reverse the word
        return variations