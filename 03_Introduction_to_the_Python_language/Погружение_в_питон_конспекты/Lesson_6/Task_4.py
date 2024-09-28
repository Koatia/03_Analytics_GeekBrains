# - Создайте модуль с функцией внутри.
# - Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# - Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

from my_package.ex4 import guessing
from typing import List

def main() -> None:
    result = guessing(riddle, possible_answers, max_attempts)
    print(f'Код: {result}\n')

if __name__ == '__main__':
    riddle: str = 'Лёгонькое, маленькое, а на крышу не закинешь?'
    possible_answers: List[str] = ['Перо', 'Пёрышко', 'перо', 'пёрышко']
    max_attempts: int = 3

    main()
