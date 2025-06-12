def setup_cli():
    import argparse

    parser = argparse.ArgumentParser(description="Smart Wordlist Generator for Cybersecurity.")
    
    parser.add_argument('--max-length', type=int, help='Maximum length of generated words.')
    parser.add_argument('--leet', action='store_true', help='Enable leetspeak mutations.')
    parser.add_argument('--capitalize', action='store_true', help='Capitalize the first letter of each word.')
    parser.add_argument('--extra', type=str, nargs='*', help='Additional words or phrases to include in the wordlist.')

    args = parser.parse_args()
    
    return args