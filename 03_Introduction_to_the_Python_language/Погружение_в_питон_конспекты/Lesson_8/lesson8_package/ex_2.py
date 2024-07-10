import os
import json
from typing import Dict


def is_id_in_file(user_data: Dict[str, Dict[str, str]], user_id: str) -> bool:
    """
    Проверяет, содержится ли заданный идентификатор пользователя в словаре user_data.

    :Аргументы:
        - user_data (Dict[str, Dict[str, str]]): Словарь с данными пользователей, организованный по уровням доступа.
        Ключи словаря - уровни доступа (строковые представления чисел от 1 до 7),
        значения - словари с идентификаторами пользователей (ключи) и их именами (значения).
        - user_id (str): Идентификатор пользователя для проверки.

    Возвращаемое значение:
        - bool: Возвращает True, если идентификатор пользователя содержится в user_data, иначе возвращает False.
    """

    for access_level in user_data.values():
        if user_id in access_level:
            return True
    return False


def add_user_to_json(path_file: str) -> None:
    """
    Обрабатывает файл с данными и сохраняет их в формате JSON.

    :Аргументы:
        - path_file (str): Путь к файлу с данными.

    Возвращаемое значение:
        - None. Функция не возвращает явно заданного значения. Данные сохраняются в файл формата JSON.


    :Формат JSON файла:
            Пример:
            {
                "1": {
                    "ID1": "Имя1",
                    "ID2": "Имя2"
                },
                "2": {
                    "ID3": "Имя3"
                },
                ...
            }
    """

    user_data: Dict[str, Dict[str, str]] = {}

    if os.path.isfile(path_file):
        with open(path_file, 'r') as file:
            user_data = json.load(file)

    while True:
        name: str = input("Введите имя пользователя: ")
        user_id: str = input("Введите ID пользователя: ")
        access_level: int = int(input("Введите уровень доступа (от 1 до 7): "))

        if access_level not in range(1, 8):
            print("Ошибка. Уровень должен быть от 1 до 7.")
            continue

        if is_id_in_file(user_data, user_id):
            print("Пользователь с таким ID уже существует.")
            continue

        if str(access_level) not in user_data:
            user_data[str(access_level)] = {}

        user_data[str(access_level)][user_id] = name
        sorted_user_data: Dict[str, Dict[str, str]] = {k: v for k, v in sorted(user_data.items(),
                                                                               key=lambda item: int(item[0]))}

        with open(path_file, 'w') as file:
            json.dump(sorted_user_data, file, indent=4, ensure_ascii=False)
