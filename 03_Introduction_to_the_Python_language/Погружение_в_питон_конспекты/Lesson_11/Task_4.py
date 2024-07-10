# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archieve():
    __instance = None

    def __init__(self, num: int, text: str) -> None:
        self.text: str = text
        self.num: int = num

    def __new__(cls, *args, **kwargs) -> 'Archieve':
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __str__(self) -> str:
        return f'\nТекст: "{self.text}"\nЧисло: "{self.num}"\nАрхив текста: "{self.text_list}"\nАрхив чисел: "{self.num_list}" '

    def __repr__(self) -> str:
        return f'\nТекст: "{self.text}"\nЧисло: "{self.num}"'


if __name__ == '__main__':
    new_arch_1 = Archieve(1, 'test_1')
    new_arch_2 = Archieve(2, 'test_2')
    print(new_arch_2.num_list)
    print(new_arch_2.text_list)

    print(new_arch_2)
    print(repr(new_arch_2))

    help(Archieve)
