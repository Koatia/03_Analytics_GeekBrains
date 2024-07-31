# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# Напишите преобразование в одну строку.

from my_package.ex2 import create_letter_code_dictionary
from typing import Dict

def main() -> None:
    text: str = "Самостоятельно сохраните в переменной строку"
    letter_codes: Dict[str, int] = create_letter_code_dictionary(text)
    print(letter_codes)

if __name__ == '__main__':
    main()

