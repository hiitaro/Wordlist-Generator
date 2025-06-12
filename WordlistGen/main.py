# Sample Output:
# daniil123
# d4n11l!
# Daniil_dev
# daaniil@
# petname2023
# hobbyname123!

import os
from core.cli import setup_cli
from core.input_handler import InputHandler
from core.mutator import Mutator
from core.combiner import Combiner
from output.writer import Writer

def main():
    args = setup_cli()
    mutator = Mutator()
    combiner = Combiner()
    writer = Writer()

    # Получение пользовательских данных только из --extra
    user_data = []
    if args.extra:
        user_data.extend(args.extra)

    # Генерация мутаций
    wordlist = []
    for word in user_data:
        wordlist.append(word)
        wordlist.extend(mutator.add_suffixes(word))
        wordlist.extend(mutator.insert_symbols(word))
        wordlist.append(mutator.repeat_letters(word))
        if args.leet:
            wordlist.append(mutator.leetspeak(word))
        wordlist.extend(mutator.case_variations(word))

    # Генерация попарных комбинаций (через дефис, подчёркивание и слитно) с мутациями
    from itertools import combinations
    pairwise = list(combinations(user_data, 2))
    combo_patterns = [
        "{w1}-{w2}",
        "{w2}-{w1}",
        "{w1}_{w2}",
        "{w2}_{w1}",
        "{w1}{w2}",
        "{w2}{w1}"
    ]
    for w1, w2 in pairwise:
        for pattern in combo_patterns:
            combo = pattern.format(w1=w1, w2=w2)
            wordlist.append(combo)
            wordlist.extend(mutator.add_suffixes(combo))
            wordlist.extend(mutator.insert_symbols(combo))
            wordlist.append(mutator.repeat_letters(combo))
            if args.leet:
                wordlist.append(mutator.leetspeak(combo))
            wordlist.extend(mutator.case_variations(combo))

    # Фильтрация по длине
    if args.max_length:
        wordlist = [w for w in wordlist if len(w) <= args.max_length]

    # Удаление дубликатов
    wordlist = writer.remove_duplicates(wordlist)

    # Создание папки output, если не существует
    os.makedirs("output", exist_ok=True)

    # Сохранение
    writer.write_to_file(wordlist, "output/wordlist.txt")
    print(f"Wordlist saved to output/wordlist.txt ({len(wordlist)} words)")

if __name__ == "__main__":
    main()