# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

my_tuple = (2, 'Hello', 5.75, True, 72, [1, 2, 3], 'World', True, False, [2, 4, 6])
my_dict = {}

for elem in my_tuple:
    elem_type = type(elem).__name__

    if elem_type not in my_dict:
        my_dict[elem_type] = []
    my_dict[elem_type].append(elem)

print(my_dict)
