# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.


# Функция создания словаря с парами ключ-значение
def create_unicode_dict_range(input_str: str) -> dict:
    numbers: list[str] = input_str.split()
    min_num: int = int(numbers[0])
    max_num: int = int(numbers[1])

    unicode_dict: dict = {}

    for num in range(min_num, max_num + 1):
        unicode_char: str = chr(num)
        unicode_dict[unicode_char] = num

    return unicode_dict

def __main() -> None:
    input_str: str = input("Введите два числа через пробел: ")
    result_dict: dict = create_unicode_dict_range(input_str)
    print(result_dict)

if __name__ == '__main__':
    __main()

