from typing import Generator

def __is_prime_number(number: int) -> bool:

    """
    Проверяет, является ли заданное число простым (не имеет делителей, кроме 1 и самого себя).

    :Аргументы:
        - number (int): Проверяемое число.

    :Возвращаемое значение:
        - bool: True, если число является простым, и False в противном случае.
    """

    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def generate_prime_numbers(indicator: int) -> Generator[int, None, None]:

    """
    Генератор, который возвращает заданное количество простых чисел.

    :Аргументы:
        - indicator (int): Количество простых чисел, которое требуется сгенерировать.

    :Возвращаемое значение:
        - Generator[int, None, None]: Итератор, возвращающий простые числа по одному по мере генерации.
    """

    count: int = 0
    number: int = 2

    while count < indicator:
        if __is_prime_number(number):
            yield number
            count += 1
        number += 1

__all__ = ['generate_prime_numbers']

