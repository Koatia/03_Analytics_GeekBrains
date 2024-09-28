import json
import os
from typing import Callable, List, Dict, Any


def logger(func: Callable) -> Callable:
    file_name: str = f'{func.__name__}.json'

    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data: List[Dict[str, Any]] = json.load(f)
    else:
        data: List[Dict[str, Any]] = []

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        json_dict: Dict[str, Any] = {'args': args, **kwargs}
        result: Any = func(*args, **kwargs)
        json_dict['result'] = result
        data.append(json_dict)

        with open(file_name, 'w', encoding='utf-8') as f1:
            json.dump(data, f1, ensure_ascii=False, indent=4)

        return result

    return wrapper


@logger
def get_summ(number_1: int, number_2: int, *args: Any, **kwargs: Any) -> int:

    """
    Функция вычисляет сумму двух чисел (number_1 и number_2) типа int, а также дополнительных
    позиционных и именованных аргументов (*args и **kwargs), если они указаны.
    Результат записывается в .json файл
    """

    result: int = number_1 + number_2
    return result
