# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

friends = {
    'Друг1': ('Рюкзак', 'Палатка', 'Ложка', 'Чашка'),
    'Друг2': ('Рюкзак', 'Ложка', 'Спички', 'Фанарик', 'Вилка'),
    'Друг3': ('Рюкзак', 'Чашка', 'Термос', 'Компас', 'Вилка'),
}

common_items = set(friends['Друг1'])
missing_items = {}

for friend in friends:
    common_items = common_items.intersection(set(friends[friend]))

unique_items = set()
all_items = set()

for items in friends.values():
    for item in items:
        if item in all_items:
            unique_items.discard(item)
        else:
            all_items.add(item)
            unique_items.add(item)

print(f'Вещи взятые всеми тремя друзьями: {common_items}')
print(f'Уникальные вещи, которые есть только у одного друга: {unique_items}')

for friend, items in friends.items():
    for item in items:
        if item not in common_items:
            if item not in missing_items:
                missing_items[item] = set()
            missing_items[item].add(friend)

print('Вещи, которые есть у всех друзей кроме одного и имя друга:')
for item, friends_set in missing_items.items():
    if len(friends_set) == len(friends) - 1:
        missing_friend = (set(friends.keys()) - friends_set).pop()
        print(f'{item}: {missing_friend}')








