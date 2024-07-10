# Напишите класс для хранения информации о человеке:
# - ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.


class Person:
    def __init__(self, surname: str, first_name: str, patronymic: str, age: int) -> None:
        self.surname: str = surname
        self.first_name: str = first_name
        self.patronymic: str = patronymic
        self.__age: int = age

    def full_name(self) -> str:
        full_name_result: str = f'{self.surname} {self.first_name} {self.patronymic}'
        return full_name_result

    def birthday(self) -> None:
        self.__age += 1

    def get_age(self) -> int:
        return self.__age


if __name__ == '__main__':
    person: Person = Person('Иванов', 'Иван', 'Иванович', 20)

    print(f'ФИО: {person.full_name()}')
    print(f'Возраст: {person.get_age()}')

    person.birthday()
    print(f'Возраст увеличенный на год: {person.get_age()}')

    # print(persen.__age)
