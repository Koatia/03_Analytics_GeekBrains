# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# - Строки нумеруются начиная с единицы.
# - Слова выводятся отсортированными согласно кодировки Unicode.
# - Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

# Функция для обработки введенных строк
def process_strings() -> None:
    data: list[str] = input('Введите строку: ').split()
    data.sort()
    max_len: int = find_max_length(data)
    print_formatted(data, max_len)


# Функция поиска максимальной длины строки из списка
def find_max_length(data: list[str]) -> int:
    max_len: int = 0
    for item in data:
        if len(item) > max_len:
            max_len = len(item)
    return max_len


# Функция форматирования результата
def print_formatted(data: list[str], max_len: int) -> None:
    for i, item in enumerate(data, 1):
        print(f'{i}. {item:>{max_len}}')


if __name__ == '__main__':
    process_strings()
