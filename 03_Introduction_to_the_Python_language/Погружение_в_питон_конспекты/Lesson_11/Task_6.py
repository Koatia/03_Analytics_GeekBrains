# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:

    def __init__(self, width: float, height: float = None) -> None:
        self.width: float = width

        if height is None:
            self.height: float = width
        else:
            self.height: float = height

    def calc_perimeter(self) -> float:
        self.perimeter: float = (self.width + self.height) * 2
        return self.perimeter

    def calc_area(self) -> float:
        self.area: float = self.width * self.height
        return self.area

    def __add__(self, other) -> "Rectangle":
        perimeter: float = self.calc_perimeter() + other.calc_perimeter()
        width: float = self.width + other.width
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other) -> "Rectangle":
        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self

        width: float = abs(self.width - other.width)
        perimeter: float = self.calc_perimeter() - other.calc_perimeter()
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self) -> str:
        return f'\nПериметр = {self.calc_perimeter()}\nДлина = {self.width}\nВысота = {self.height}\n'

    def __eq__(self, other: object) -> bool:
        return self.calc_area() == other.calc_area()

    def __lt__(self, other: object) -> bool:
        return self.calc_area() < other.calc_area()

    def __le__(self, other: object) -> bool:
        return self.calc_area() <= other.calc_area()

    def print_info(self):
        print(self)


if __name__ == '__main__':
    first_rectangle: Rectangle = Rectangle(5, 30)
    second_rectangle: Rectangle = Rectangle(30, 5)

    first_rectangle.print_info()
    second_rectangle.print_info()

    print("Площади равны:", first_rectangle == second_rectangle)
    print("Площадь нового прямоугольника меньше:", first_rectangle < second_rectangle)
    print("Площадь нового прямоугольника меньше или равна:", first_rectangle <= second_rectangle)
