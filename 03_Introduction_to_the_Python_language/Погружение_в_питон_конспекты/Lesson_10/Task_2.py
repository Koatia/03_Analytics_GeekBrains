# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class MyRectangle:
    def __init__(self, width: float, height: float = None) -> None:
        self.width: float = width
        self.height: float = width if height is None else height

    def calculate_perimeter(self) -> float:
        perimeter: float = (self.width + self.height) * 2
        return perimeter

    def calculate_area(self) -> float:
        area: float = self.width * self.height
        return area


if __name__ == '__main__':
    WIDTH: float = 10
    HEIGHT: float = 20

    new_rectangle: MyRectangle = MyRectangle(WIDTH, HEIGHT)
    new_square: MyRectangle = MyRectangle(WIDTH)

    print(new_rectangle.calculate_perimeter())
    print(new_rectangle.calculate_area())

    print(new_square.calculate_perimeter())
    print(new_square.calculate_area())
