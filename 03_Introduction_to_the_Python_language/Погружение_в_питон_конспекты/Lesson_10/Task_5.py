# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    def __init__(self, name: str, length: int, small_length_threshold: int, large_length_threshold: int) -> None:
        self.name = name
        self.length: int = length
        self.SMALL_LENGTH_THRESHOLD: int = small_length_threshold
        self.LARGE_LENGTH_THRESHOLD: int = large_length_threshold

    def fish_size(self) -> str:
        if self.length < self.SMALL_LENGTH_THRESHOLD:
            return 'Рыба небольшого размера'
        elif self.length > self.LARGE_LENGTH_THRESHOLD:
            return 'Рыба большого размера'
        else:
            return 'Рыба среднего размера'


class Bird:
    def __init__(self, name: str, wings: int) -> None:
        self.name = name
        self.wings: int = wings

    def wingspan(self) -> str:
        return f'Размах крыльев: {self.wings * 2}'

class Mammal:
    def __init__(self, name: str, fur_color: str, has_tail: bool) -> None:
        self.name = name
        self.fur_color: str = fur_color
        self.has_tail: bool = has_tail

    def description(self) -> str:
        tail_info = "имеет хвост" if self.has_tail else "не имеет хвоста"
        return f'{self.name} - млекопитающее с {self.fur_color} окрасом и {tail_info}.'


if __name__ == '__main__':
    SMALL_LENGTH_THRESHOLD: int = 10
    LARGE_LENGTH_THRESHOLD: int = 100

    shark: Fish = Fish('Акула', 50, SMALL_LENGTH_THRESHOLD, LARGE_LENGTH_THRESHOLD)
    print(shark.fish_size())

    eagle: Bird = Bird('Орёл', 15)
    print(eagle.wingspan())

    lion: Mammal = Mammal('Кит', 'черно-белым', True)
    print(lion.description())
