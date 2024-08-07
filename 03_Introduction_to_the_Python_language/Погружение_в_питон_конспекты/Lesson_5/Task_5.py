# Напишите программу, которая выводит на экран числа от 1 до 100.
# - При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# - Вместо чисел, кратных пяти — слово «Buzz».
# - Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# - *Превратите решение в генераторное выражение.

from my_package.ex5 import fizz_buzz_generator

def main() -> None:
    for result in fizz_buzz_generator():
        print(result, end=' ')


if __name__ == '__main__':
    main()

