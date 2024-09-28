# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi


class MyCircle:
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def calculate_perimeter(self) -> float:
        perimeter: float = 2 * pi * self.radius
        return perimeter

    def calculate_area(self) -> float:
        area: float = pi * self.radius ** 2
        return area


if __name__ == '__main__':
    RADIUS: float = 5

    new_circle: MyCircle = MyCircle(RADIUS)

    print(new_circle.calculate_perimeter())
    print(new_circle.calculate_area())
