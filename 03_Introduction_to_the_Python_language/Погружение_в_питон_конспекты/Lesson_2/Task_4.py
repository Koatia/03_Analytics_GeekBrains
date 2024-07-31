# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

from decimal import Decimal, getcontext
from math import pi

getcontext().prec = 42

user_input: str = '\nВведите диаметр окружности от 1 до 1000: '
number_pi: Decimal = Decimal(pi)

while True:
    diametr: Decimal = Decimal(input(user_input))

    if 0 < diametr <= 1000:
        area: Decimal = number_pi * (diametr**2 / 4)
        print(f'\nПлощадь круга с диаметром {diametr}: {area}')

        length: Decimal = number_pi * diametr
        print(f'Длина окружности с диаметром {diametr}: {length}')

        break

    else:
        user_input = f'Число {diametr} выходит за рамки диапазона, повторите попытку!' \
                     f'\n\nВведите диаметр окружности от 1 до 1000: '
