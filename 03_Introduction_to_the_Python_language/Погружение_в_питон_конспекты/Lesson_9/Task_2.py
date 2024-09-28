# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию - угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from Lesson_9.lesson9_package import number_guessing_game

SECRET_NUMBER: int = 125
NUMBER_OF_ATTEMPTS: int = 11


def main() -> None:
    number_guessing_game(SECRET_NUMBER, NUMBER_OF_ATTEMPTS)


if __name__ == '__main__':
    main()
