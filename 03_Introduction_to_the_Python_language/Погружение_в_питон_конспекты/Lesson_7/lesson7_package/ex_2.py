from random import randint, choice

VOWELS: str = 'aeiou'
CONSONANTS: str = 'bcdfghjklmnpqrstvwxyz'


def generate_pseudo_names(num_names: int, file_name: str, length_min: int, length_max: int) -> None:
    """
    Генерирует псевдонимы из случайных букв для заданного числа раз и записывает их в указанный файл.

    :Аргументы:
        - num_names (int): Желаемое количество псевдонимов для генерации.
        - file_name (str): Имя файла, в который будут записаны сгенерированные псевдонимы.
        - length_min (int): Минимальная длина генерируемого псевдонима (количество символов).
        - length_max (int): Максимальная длина генерируемого псевдонима (количество символов).

    :Глобальные переменные:
        - VOWELS (str): Строка, содержащая гласные буквы.
        - CONSONANTS (str): Строка, содержащая согласные буквы.

    :Возвращаемое значение:
        - None: Функция не возвращает явно заданного значения. Псевдонимы записываются в указанный файл.
    """

    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_names):
            name: str = ''.join(choice(VOWELS) if i in (1, 4, 6) else choice(CONSONANTS)
                                for i in range(randint(length_min, length_max)))

            f.write(name.capitalize() + '\n')
