# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from my_package.ex5 import guesses_dict
from typing import Dict, List

def main() -> None:
    riddles_and_nswers: Dict[str, List[str]] = {'Лёгонькое, маленькое, а на крышу не закинешь?': ['Перо', 'Пёрышко', 'перо', 'пёрышко'],
                          'Что можно встретить один раз в минуту, два раза в моменте и ни разу в тысяче лет?': ['Букву М', 'Буква М', 'М', 'м'],
                          'Красна девица сидит в темнице, а коса на улице?': ['Морковь', 'Морковка', 'морковь', 'морковка'],
                          'Жидкое, а не вода, белое, а не снег': ['Молоко', 'молоко', 'Молочко', 'молочко']}
    max_attempts: int = 3

    guesses_dict(riddles_and_nswers, max_attempts)


if __name__ == '__main__':
    main()

