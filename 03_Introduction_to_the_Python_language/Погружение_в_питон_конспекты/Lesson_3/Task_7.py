# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

data = input('Введите строку текста: ')
my_dict = {}

for elem in data:
    count = data.count(elem)
    my_dict[elem] = count

for element, count in my_dict.items():
    print(f'Ключ: {element}; Значение: {count}')

# data = input('Введите строку текста: ')
# my_dict = {}

# for elem in data:
#     if elem in my_dict:
#         my_dict[elem] += 1
#     else:
#         my_dict[elem] = 1

# for element, count in my_dict.items():
#     print(f'Ключ: {element}; Значение: {count}')

