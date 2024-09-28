# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# Функция сортировки пузыркем
def bubble_sort(number_list: list[int]) -> None:
    list_length: int = len(number_list)
    for i in range(list_length - 1):
        for j in range(list_length - 1 - i):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]

def __main() -> None:
    numbers: list[int] = [9, 2, 7, 4, 5]
    bubble_sort(numbers)
    print(numbers)

if __name__ == '__main__':
    __main()
