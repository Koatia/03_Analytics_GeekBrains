# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# - расширение
# - минимальная длина случайно сгенерированного имени, по умолчанию 6
# - максимальная длина случайно сгенерированного имени, по умолчанию 30
# - минимальное число случайных байт, записанных в файл, по умолчанию 256
# - максимальное число случайных байт, записанных в файл, по умолчанию 4096
# - количество файлов, по умолчанию 10
# - Имя файла и его размер должны быть в рамках переданного диапазона.

from Lesson_7.lesson7_package import gen_ext


def main():
    gen_ext('txt')


if __name__ == '__main__':
    main()
