from my_package.ex4 import guessing
from typing import Dict, List

__result: Dict[str, int] = {}

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
        res: int = guessing(key, value, count)
        __result_score(key, res)

    __printing_statistic()


def __result_score(text: str, count: int) -> None:
    __result.update({text: count})

def __printing_statistic() -> None:
    statistic: str = '\n'.join(
        f'Загадка: "{key}": использовано попыток - {value}' if value > 0
        else f'Загадка: "{key}": вы не угадали загадку'
        for key, value in __result.items()
    )
    print(f'Статистика:\n{statistic}')

__all__ = ['guesses_dict']
