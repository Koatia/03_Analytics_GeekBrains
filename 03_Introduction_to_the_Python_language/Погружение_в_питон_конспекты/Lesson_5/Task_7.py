# Создайте функцию-генератор.
# - Функция генерирует N простых чисел, начиная с числа 2.
# - Для проверки числа на простоту используйте правило:
#     «число является простым, если делится нацело только на единицу и на себя».

from my_package.ex7 import generate_prime_numbers
from typing import List


def main() -> None:
    numeric_indicator: int = 10
    prime_numbers: List[int] = list(generate_prime_numbers(numeric_indicator))
    print(prime_numbers)


if __name__ == '__main__':
    main()

