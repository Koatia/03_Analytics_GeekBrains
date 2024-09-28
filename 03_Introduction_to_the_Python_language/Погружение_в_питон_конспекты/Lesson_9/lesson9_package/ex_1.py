from typing import Callable


def guess_number(number: int, count: int) -> Callable[[], None]:
    """
    Функция принимает на вход загаданное число и максимальное количество попыток.
    Возвращает внутреннюю функцию make_guess, которая предоставляет пользователю возможность угадать число.
    """

    def make_guess():
        for i in range(1, count + 1):
            print(f'Попытка № {i}. Осталось попыток: {count - i + 1}')

            num_input: int = int(input('Введите число: '))

            if num_input == number:
                print('Вы угадали!')
                break
            elif num_input < number:
                print('Ваше число меньше!')
            else:
                print('Ваше число больше!')

    return make_guess()
