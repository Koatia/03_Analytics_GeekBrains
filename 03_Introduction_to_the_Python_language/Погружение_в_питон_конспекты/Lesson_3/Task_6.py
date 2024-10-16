# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

data = input('Введите строку: ').split()

data.sort()
max_len = 0

for item in data:
    if len(item) > max_len:
        max_len = len(item)

for i, item in enumerate(data, 1):
    print(f'{i}. {item:>{max_len}}')
