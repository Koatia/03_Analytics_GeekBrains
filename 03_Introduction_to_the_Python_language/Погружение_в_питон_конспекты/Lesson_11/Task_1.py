# Создайте класс Моя Строка, где:
# - будут доступны все возможности str
# - дополнительно хранятся имя автора строки и время создания (time.time)

from time import time


class My_string(str):
    def __new__(cls, value: str, author_name: str) -> 'My_string':
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.time_created = time()
        print(f'Создал класс: {cls}')
        return instance


if __name__ == '__main__':
    new_str: My_string = My_string('Тест строки', 'New Name')
    print(new_str.author_name)
    print(new_str.time_created)

    print(My_string.__doc__)
    print(My_string.__new__.__doc__)
