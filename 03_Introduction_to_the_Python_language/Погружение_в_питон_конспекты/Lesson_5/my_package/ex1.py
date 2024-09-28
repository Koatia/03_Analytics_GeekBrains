from typing import Dict, List, Tuple

def dictionary_from_input() -> Dict[int, Tuple[int, ...]]:

    """
    Принимает пользовательский ввод в виде строки, состоящей из четырех или более целых чисел,
    разделенных символом "/". Возвращает словарь с двумя ключами: второе число ввода становится
    ключом для первого числа, а третье число становится ключом для кортежа, содержащего оставшиеся числа.

    :Возвращаемое значение:
        - Словарь с целочисленными ключами и значениями типа кортеж.
    """

    input_string: str = input('Введите строку из четырех или более целых чисел, разделенных символом "/": ')
    numbers: List[int] = list(map(int, input_string.split('/')))

    result_dict: Dict[int, Tuple[int, ...]] = {numbers[1]: numbers[0], numbers[2]: tuple(numbers[3:])}

    return result_dict

__all__ = ['dictionary_from_input']
