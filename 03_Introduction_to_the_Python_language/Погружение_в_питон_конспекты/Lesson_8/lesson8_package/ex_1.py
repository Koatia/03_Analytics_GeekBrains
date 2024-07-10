import json
from typing import Any


def fail_to_json(path: str) -> None:
    """
    Обрабатывает файл с данными и сохраняет их в формате JSON.

    :Аргументы:
        - path (str): Путь к файлу с данными.

    :Возвращаемое значение:
        - None: Функция не возвращает явно заданного значения. Данные сохраняются в файл формата JSON.

    :Формат JSON файла:
        - Сгенерированный JSON файл содержит данные в формате словаря, в котором ключи - имена (с заглавной буквы),
        а значения - числа в формате с плавающей запятой.
    """

    my_dict: dict[Any, float] = {}

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split(' ')
            my_dict[name.capitalize()] = float(number)
    print(my_dict)

    with open('Task_1.json', 'w', encoding='utf-8') as j:
        json.dump(my_dict, j, ensure_ascii=False, indent=4)
