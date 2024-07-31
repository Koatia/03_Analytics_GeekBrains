# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

TWO = 2
my_list = [1, 1, 1, 2, 2, 2, 4, 4, 5, 7, 8, 9, 9]

for element in set(my_list):
    if my_list.count(element) == TWO:
        for _ in range(TWO):
            my_list.remove(element)
print(my_list)
