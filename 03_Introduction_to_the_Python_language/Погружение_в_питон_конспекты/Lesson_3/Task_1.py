# ✔ Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.


my_list = [1, 7, 4, 3, 4, 1, 7, 6, 5, 5, 3, 2]

# Короткое решение
new_list = list(set(my_list))
print(new_list)


# Длинное решение
new_list = []

for elem in my_list:
    if elem not in new_list:
        new_list.append(elem)
print(new_list)
