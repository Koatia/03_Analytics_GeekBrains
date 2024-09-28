from random import randint

def guess_num(min_num: int, max_num: int, counts: int) -> bool:

    """
    Функция для угадывания числа.

    :Аргументы:
        - min_num (int): Минимальное число в диапазоне для угадывания.
        - max_num (int): Максимальное число в диапазоне для угадывания.
        - counts (int): Максимальное количество попыток угадывания.

    :Возвращаемое значение:
        - bool: True, если число было угадано, False в противном случае.
    """

    number: int = randint(min_num, max_num)

    for _ in range(counts):
        current_num: int = int(input(f'Введите число от {min_num} до {max_num}: '))

        if current_num < number:
            print(f'Искомое число больше этого')
        elif current_num > number:
            print(f'Искомое число меньше этого')
        else:
            print('Вы угадали!')
            return True

    print(f'Попытки закончились, вы не угадали число {number}!')
    return False

__all__ = ['guess_num']
