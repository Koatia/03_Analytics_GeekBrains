# - Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# - Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# - Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from my_package.ex2 import guess_num
from typing import Generator
from sys import argv

def main() -> None:
    x: Generator[int, None, None] = (int(i) for i in argv[1:])
    guess_num(*x)


if __name__ == '__main__':
    main()

