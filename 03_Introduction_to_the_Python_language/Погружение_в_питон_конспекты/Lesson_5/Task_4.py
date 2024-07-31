# Создайте генератор чётных чисел от нуля до 100.
# - Из последовательности исключите числа, сумма цифр которых равна 8.
# - Решение в одну строку.

from my_package.ex4 import exclude_numbers_with_sum_of_digits_8

def main() -> None:
    for result in exclude_numbers_with_sum_of_digits_8():
        print(result, end=' ')


if __name__ == '__main__':
    main()

