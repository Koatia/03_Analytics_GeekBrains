# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# - шестизначный идентификационный номер
# - уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from Task_3 import Person

class Employee(Person):
    def __init__(self, surname: str, first_name: str, patronymic: str, age: int, employee_id: int, min_id: int,
                 max_id: int) -> None:
        super().__init__(surname, first_name, patronymic, age)

        self.employee_id: int = employee_id if min_id <= employee_id <= max_id else min_id

    def get_level(self, access_level: int) -> int:
        sum_digits_id: int = sum(int(num) for num in str(self.employee_id))
        return sum_digits_id % access_level


if __name__ == '__main__':
    MIN_IDENTIFIER: int = 100_000
    MAX_IDENTIFIER: int = 999_999
    MAX_ACCESS_LEVEL: int = 7

    empl_instance: Employee = Employee('Иванов', 'Иван', 'Иванович', 20, 123460, MIN_IDENTIFIER, MAX_IDENTIFIER)

    print(f'\nУровень доступа сотрудника {empl_instance.full_name()}: {empl_instance.get_level(MAX_ACCESS_LEVEL)}')
