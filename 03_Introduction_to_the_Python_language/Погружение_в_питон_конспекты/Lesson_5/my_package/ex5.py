from typing import Generator, Union

def fizz_buzz_generator() -> Generator[Union[str, int], None, None]:

    """
    Генератор, который создает последовательность чисел от 1 до 100 (включительно)
    и заменяет числа, которые делятся на 3 на "Fizz", числа, которые делятся на 5 на "Buzz",
    и числа, которые делятся на и 3, и на 5 на "FizzBuzz".

    :Возвращаемое значение:
        - Generator[Union[str, int], None, None]: Итератор, возвращающий либо числа, либо строки "Fizz", "Buzz" или "FizzBuzz".
    """

    fizz_buzz = ("FizzBuzz" if num % 15 == 0
                 else "Fizz" if num % 3 == 0
                 else "Buzz" if num % 5 == 0
                 else num for num in range(1, 101))
    return fizz_buzz


__all__ = ['fizz_buzz_generator']
