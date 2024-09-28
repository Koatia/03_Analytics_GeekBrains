# Добавьте к задачам 1 и 2 строки документации для классов.

from time import time


class My_string(str):
    """
    Класс My_string наследуется от стандартного класса str и добавляет дополнительные атрибуты.
    """

    def __new__(cls, value: str, author_name: str) -> 'My_string':
        """
        Создание нового объект My_string.
        """

        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.time_creared = time()
        print(f'Создал класс: {cls}')

        return instance


class Archieve():
    """
    Класс для архивирования данных
    """
    __instance = None

    def __init__(self, num: int, text: str) -> None:

        """
        Инициализация экземпляра класса
        """

        self.text: str = text
        self.num: int = num

    def __new__(cls, *args, **kwargs) -> 'Archieve':

        """
        Создание единственного экземпляра класса Archieve или возврат существующего
        """

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance


if __name__ == '__main__':
    print(f'\nЗадача 1:\n{My_string.__doc__}')
    print(f'Задача 2:\n{Archieve.__doc__}')
