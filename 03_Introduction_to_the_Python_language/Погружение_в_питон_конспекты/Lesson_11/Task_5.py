# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


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

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        perimeter: float = self.calc_perimeter() + other.calc_perimeter()
        width: float = self.width + other.width
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other: 'Rectangle') -> 'Rectangle':
        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self

        width: float = abs(self.width - other.width)
        perimeter: float = self.calc_perimeter() - other.calc_perimeter()
        height: float = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self) -> str:
        return f'Периметр = {self.calc_perimeter()}\nДлина = {self.width}\nВысота = {self.height}'


if __name__ == '__main__':
    first_rectangle: Rectangle = Rectangle(10, 20)
    second_rectangle: Rectangle = Rectangle(5)
    print(f'Первый прямоугольник:\n{first_rectangle + second_rectangle}')
    print(f'\nВторой прямоугольник:\n{first_rectangle - second_rectangle}')
