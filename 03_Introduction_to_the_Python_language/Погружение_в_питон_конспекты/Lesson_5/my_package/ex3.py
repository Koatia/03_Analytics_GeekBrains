from typing import Dict, Iterator, Tuple

def create_letter_code_dictionary(text: str) -> Dict[str, int]:

    """
    Создает словарь, который сопоставляет каждый символ из входной строки
    с его числовым значением (кодом символа Unicode).

    :Аргументы:
        - text (str): Входная строка, для которой нужно создать словарь.

    :Возвращаемое значение:
        - Dict[str, int]: Словарь, в котором ключами являются символы из входной строки,
          а значениями - их числовые коды Unicode.
    """

    text_dict: Dict[str, int] = {char: ord(char) for char in text}
    return text_dict


def get_first_five_pairs(dictionary: Dict[str, int], count: int) -> None:

    """
    Функция выводит первые пять пар (ключ, значение) из переданного словаря.

    :Аргументы:
        - dictionary (Dict[str, int]): Словарь, из которого будут взяты первые пять пар.
        - count (int): Количество пар для вывода.

    :Возвращаемое значение:
        None: Функция ничего не возвращает, только выводит результаты на экран.
    """

    iterator: Iterator[Tuple[str, int]] = iter(dictionary.items())
    for _ in range(count):
        print(next(iterator), end=' ')


__all__ = ['create_letter_code_dictionary', 'get_first_five_pairs']

