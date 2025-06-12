class InputHandler:
    def __init__(self):
        self.args = None
        self.config = {}

    def parse_args(self):
        import argparse
        parser = argparse.ArgumentParser(description="Smart Wordlist Generator")
        parser.add_argument('--config', type=str, help='Path to configuration file')
        parser.add_argument('--max-length', type=int, default=20, help='Maximum length of generated words')
        parser.add_argument('--leet', action='store_true', help='Enable leetspeak mutations')
        parser.add_argument('--capitalize', action='store_true', help='Capitalize words')
        parser.add_argument('--extra', type=str, nargs='*', help='Extra words to include in the wordlist')
        self.args = parser.parse_args()

    def load_config(self, config_path):
        import json
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)