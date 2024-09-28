from typing import Callable, Any
from random import randint


def check_parametr(func: Callable) -> Callable:
    MIN_NUM: int = 1
    MAX_NUM: int = 100
    MIN_COUNT: int = 1
    MAX_COUNT: int = 10

    def wrapper(number: int, count: int, *args: Any, **kwargs: Any) -> Any:
        if number > MAX_NUM or number < MIN_NUM:
            number = randint(MIN_NUM, MAX_NUM)
            print(f'\nСлучайное число = {number}\n')

        if count > MAX_COUNT or count < MIN_COUNT:
            count = randint(MIN_COUNT, MAX_COUNT)

        result: Any = func(number, count, *args, **kwargs)

        return result

    return wrapper


@check_parametr
def number_guessing_game(number: int, count: int) -> Callable[[], None]:

    """
    Функция угадывания числа. Пользователь должен угадать число за count попыток, которое выбрано заранее.

    Если значение number выходит за пределы диапазона [MIN_NUM, MAX_NUM],
    функция выбирает случайное число в этом диапазоне.
    Если значение count выходит за пределы диапазона [MIN_COUNT, MAX_COUNT],
    функция выбирает случайное число в этом диапазоне.
    """

    def make_guess() -> None:
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
