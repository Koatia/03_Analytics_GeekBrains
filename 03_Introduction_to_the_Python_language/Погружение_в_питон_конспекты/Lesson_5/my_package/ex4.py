from typing import Iterator

def exclude_numbers_with_sum_of_digits_8() -> Iterator[int]:

    """
    Генератор, который возвращает все четные числа в диапазоне от 0 до 100 (включительно),
    у которых сумма цифр не равна 8.

    :Возвращаемое значение:
        - Iterator[int]: Итератор, возвращающий числа с условием исключения суммы цифр равной 8.
    """

    numbers_with_sum_not_8 = (num for num in range(0, 101, 2) if (num // 10 + num % 10) != 8)
    return numbers_with_sum_not_8


__all__ = ['exclude_numbers_with_sum_of_digits_8']
