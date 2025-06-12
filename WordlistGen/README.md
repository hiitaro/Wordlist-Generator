# SmartWordlistGen

SmartWordlistGen is a smart wordlist generator designed for cybersecurity purposes. It provides a modular structure that allows users to generate customized wordlists based on their specific needs. The project supports various features such as user data input, word mutations, template-based combinations, and command-line flags.

## Features

- **User Data Input**: Easily input user data through the command line or configuration files.
- **Word Mutations**: Generate variations of words using methods like letter repetition, leetspeak substitutions, case variations, suffix additions, and symbol insertions.
- **Template-Based Combinations**: Combine user data with predefined templates to create unique wordlist entries.
- **Command-Line Interface**: Utilize command-line flags for customization, including options for maximum length, leetspeak, capitalization, and additional variations.

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

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To generate a wordlist, run the application from the command line:

```
python main.py --input <user_data> --max-length <length> --leet --capitalize --extra
```

### Example

```
python main.py --input "Daniil" --max-length 12 --leet --capitalize
```

### Sample Output

# Sample Output:
# daniil123
# d4n11l!
# Daniil_dev
# daaniil@
# petname2023
# hobbyname123!

## Customization

Users can customize the wordlist generation process by modifying the default presets located in the `presets/default_presets.py` file. Additionally, users can create their own templates for more tailored wordlist combinations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.