from typing import Dict

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


__all__ = ['create_letter_code_dictionary']
