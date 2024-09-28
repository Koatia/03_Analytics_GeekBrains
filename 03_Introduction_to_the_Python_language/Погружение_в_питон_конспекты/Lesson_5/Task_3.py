# Продолжаем развивать задачу 2.
# - Возьмите словарь, который вы получили. Сохраните его итератор.
# - Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

from my_package.ex3 import create_letter_code_dictionary, get_first_five_pairs
from typing import Dict

def main() -> None:

    text: str = "Самостоятельно сохраните в переменной строку"
    letter_codes: Dict[str, int] = create_letter_code_dictionary(text)

    COUNT = 5
    get_first_five_pairs(letter_codes, COUNT)


if __name__ == '__main__':
    main()

