# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

from random import randint

MIN_RANDOM_LIST: int = 5
MAX_RANDOM_LIST: int = 11
MIN_RANDOM_NUM: int = 1
MAX_RANDOM_NUM: int = 26

# Функция вычисления суммы чисел в списке в заданном диапазоне индексов
def sum_between_indexes(numbers: list[int], start_range: int, end_range: int) -> int:
    if start_range >= len(numbers):
        start_range = len(numbers) - 1
    if end_range >= len(numbers):
        end_range = len(numbers) - 1

    if start_range < 0:
        start_range = 0
    if end_range < 0:
        end_range = 0

    start_index: int = min(start_range, end_range)
    end_index: int = max(start_range, end_range)

    total_sum: int = sum(numbers[start_index:end_index + 1])

    return total_sum

def __main() -> None:
    random_list_length: int = randint(MIN_RANDOM_LIST, MAX_RANDOM_LIST)
    random_numbers: list[int] = [randint(MIN_RANDOM_NUM, MAX_RANDOM_NUM) for _ in range(random_list_length)]
    print(random_numbers)

    start_range: int = int(input("Введите первый индекс: "))
    end_range: int = int(input("Введите второй индекс: "))

    result: int = sum_between_indexes(random_numbers, start_range, end_range)
    print("Сумма чисел в заданном диапазоне:", result)

if __name__ == '__main__':
    __main()

