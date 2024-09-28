# Создайте функцию-замыкание, которая запрашивает два целых числа:
# - от 1 до 100 для загадывания,
# - от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from Lesson_9.lesson9_package import guess_number

SECRET_NUMBER = 25
NUMBER_OF_ATTEMPTS = 5


def main() -> None:
    guess_number(SECRET_NUMBER, NUMBER_OF_ATTEMPTS)


if __name__ == '__main__':
    main()
