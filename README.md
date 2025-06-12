# 🚀 Wordlist Generator

Wordlist Generator is an advanced, customizable wordlist generator designed for cybersecurity, penetration testing, and password auditing tasks. The utility allows you to flexibly create custom wordlists based on user data, mutations, templates, and additional command-line options.

---

## 🧠 How It Works

### Architecture Overview

The project is modular and organized as follows:

- **core/** — Main logic for wordlist generation (CLI, input processing, mutations, combinatorics)
- **output/** — Handles saving results to files
- **presets/** — (Reserved for templates and presets)
- **tests/** — Unit tests for core components
- **main.py** — Entry point that connects all modules

### Detailed Workflow

1. **Command-Line Argument Parsing**  
   The CLI is built using [`setup_cli`](core/cli.py), which collects launch parameters such as maximum word length, leetspeak toggling, capitalization, and extra words.

2. **User Data Collection**  
   Currently, user data is provided via the `--extra` argument. You can supply names, nicknames, hobbies, or any relevant keywords.

3. **Mutation Generation**  
   For each user-supplied word, the [`Mutator`](core/mutator.py) module applies a variety of transformations:
   - **Letter repetition** (e.g., `daaniil`)
   - **Leetspeak** substitutions (e.g., `d4n11l`)
   - **Case variations** (all possible upper/lowercase combinations)
   - **Suffixes** (e.g., `123`, `!`, `_dev`, `2023`)
   - **Insertion of special characters** at different positions

4. **Combinatorial Generation**  
   All pairs of user words are combined using different patterns (e.g., joined, hyphenated, underscored), and mutations are applied to these combinations as well.

5. **Length Filtering**  
   If a maximum length (`--max-length`) is specified, all words exceeding this length are filtered out.

6. **Duplicate Removal**  
   The [`Writer.remove_duplicates`](output/writer.py) function ensures the final wordlist contains only unique entries.

7. **Saving the Result**  
   The final wordlist is saved to `output/wordlist.txt`.

## Project Structure

```
SmartWordlistGen
├── core
│   ├── __init__.py
│   ├── input_handler.py
│   ├── mutator.py
│   ├── combiner.py
│   └── cli.py
├── presets
│   ├── __init__.py
│   └── default_presets.py
├── output
│   ├── __init__.py
│   └── writer.py
├── tests
│   ├── __init__.py
│   ├── test_input_handler.py
│   ├── test_mutator.py
│   ├── test_combiner.py
│   └── test_writer.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository or download the source code:
   ```shell
   git clone https://github.com/hiitaro/Wordlist-Generator.git
   python WordlistGen/main.py
   ```
3. Install dependencies:
   ```shell
   pip install -r requirements.txt
   ```

---

## 🏃 Usage

Run the generator from the command line:

```shell
python main.py --extra <word1> <word2> ... [--max-length N] [--leet] [--capitalize]
```

### Command-Line Arguments

- `--extra` — Additional words or phrases for wordlist generation (required)
- `--max-length` — Maximum length of generated words (default: unlimited)
- `--leet` — Enable leetspeak variants
- `--capitalize` — Enable variants with capitalized letters (currently affects only templates, not mutations)

### Example

```shell
python main.py --extra Maria 1990 Football Ben --leet --capitalize --max-length 12
```

**Result:**  
A file named `wordlist.txt` will appear in the `output/` directory, containing unique words generated from your input and selected options.

---

## 📄 Example Output (`output/wordlist.txt`)

```
1990Maria!
MARIA-bEn
fOOTBaLL_bEn
ben-footBall
FoOTBAlLBeN
beNfOotBalL
1990_Ben%
FOOTbalLBen
Ben-FOOTBaLl
ben_FOOTbALL
BeN_foOtBAlL
BeNfooTbALl
FoOtbaLL-BEN
bEnFoOtBAll
FOotBallbEn
footbALl-BEN
Ben@Maria
BENfootBALl
Ben_^Maria
bEN-Maria
foOtballbeN
...
```
#### and 16303 words more.
---

## 🛠️ Customization & Extending

- **Add new mutations:** Extend the [`Mutator`](core/mutator.py) class with your own mutation methods.
- **Add new combination patterns:** Edit the `combo_patterns` list in [`main.py`](main.py).
- **Integrate presets or templates:** Place your files in the [`presets/`](presets/) directory and update the logic as needed.

---

## 🤝 Contributing

Pull requests and suggestions are welcome!
