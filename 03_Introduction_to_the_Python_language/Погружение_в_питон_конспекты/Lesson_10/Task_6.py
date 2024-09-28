# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

from typing import List, Union


class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def display_special_feature(self) -> None:
        pass


class Fish(Animal):
    def __init__(self, name: str, length: int, small_length_threshold: int, large_length_threshold: int) -> None:
        super().__init__(name)
        self.length: int = length
        self.SMALL_LENGTH_THRESHOLD: int = small_length_threshold
        self.LARGE_LENGTH_THRESHOLD: int = large_length_threshold

    def display_special_feature(self) -> str:
        if self.length < self.SMALL_LENGTH_THRESHOLD:
            return 'Рыба небольшого размера'
        elif self.length > self.LARGE_LENGTH_THRESHOLD:
            return 'Рыба большого размера'
        else:
            return 'Рыба среднего размера'


class Bird(Animal):
    def __init__(self, name: str, wingspan: int) -> None:
        super().__init__(name)
        self.wingspan: int = wingspan

    def display_special_feature(self) -> str:
        return f'Размах крыльев: {self.wingspan * 2}'


class Mammal(Animal):
    def __init__(self, name: str, fur_color: str, has_tail: bool) -> None:
        super().__init__(name)
        self.fur_color: str = fur_color
        self.has_tail: bool = has_tail

    def display_special_feature(self) -> str:
        tail_info = "имеет хвост" if self.has_tail else "не имеет хвоста"
        return f'{self.name} - млекопитающее с {self.fur_color} окрасом и {tail_info}.'


if __name__ == '__main__':
    SMALL_LENGTH_THRESHOLD: int = 10
    LARGE_LENGTH_THRESHOLD: int = 100

    fish_1: Fish = Fish('Акула', 50, SMALL_LENGTH_THRESHOLD, LARGE_LENGTH_THRESHOLD)
    bird_1: Bird = Bird('Орёл', 15)
    mammal_1: Mammal = Mammal('Кит', 'черно-белым', True)

    animal_list: List[Union[Fish, Bird, Mammal]] = [fish_1, bird_1, mammal_1]

    for animal in animal_list:
        print(animal.display_special_feature())
