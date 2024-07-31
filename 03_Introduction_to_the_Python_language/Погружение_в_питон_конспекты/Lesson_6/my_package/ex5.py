from my_package.ex4 import guessing
from typing import Dict, List


def guesses_dict(riddles: Dict[str, List[str]], count: int) -> None:

    """
    Эта функция принимает словарь загадок и их возможных ответов, а затем предлагает пользователям угадать ответы на каждую загадку.

    :Аргументы:
        - riddles (Dict[str, List[str]]): Словарь, где каждый ключ - загадка, а соответствующее значение - список возможных ответов на эту загадку.
        - count (int): Максимальное количество попыток для угадывания каждой загадки.

    :Возвращаемое значение:
        - None
    """

    for key, value in riddles.items():
        guessing(key, value, count)

__all__ = ['guesses_dict']
