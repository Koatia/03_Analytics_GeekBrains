# Напишите функцию, которая генерирует псевдоимена.
# - Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# - Полученные имена сохраните в файл.

from Lesson_7.lesson7_package import generate_pseudo_names

NAME_LENGTH_MIN: int = 4
NAME_LENGTH_MAX: int = 7


def main() -> None:
    generate_pseudo_names(10, 'Task_2.txt', NAME_LENGTH_MIN, NAME_LENGTH_MAX)


if __name__ == '__main__':
    main()
