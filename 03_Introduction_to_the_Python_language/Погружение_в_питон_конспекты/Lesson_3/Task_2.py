# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

data: str = input('\nВведите строку: ')
result = ''

if data.isdigit():
    number: int = int(data)

    if number > 0:
        result = f'Вы ввели целое положительное число: {number}'
    else:
        result = 'Вы ввели число ноль'

elif data.count('.') == 1 and data.replace('.', '').replace('-', '', 1).isdigit():
    try:
        number: float = float(data)

        if number > 0:
            result = f'Вы ввели положительное вещественное число: {number}'
        elif number < 0:
            result = f'Вы ввели отрицательное вещественное число: {number}'
        else:
            result = 'Вы ввели число ноль'

    except ValueError:
        result = 'Вы ввели строку без заглавной буквы'

elif any(element.isupper() for element in data):
    data_new = data.lower()
    result = f'В строке {data} есть заглавная буква, новая строка: {data_new}'

else:
    result = 'Вы ввели строку без заглавной буквы'

print(result)
