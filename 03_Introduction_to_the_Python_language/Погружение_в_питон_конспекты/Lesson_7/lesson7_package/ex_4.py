from random import choices, randint
from string import ascii_lowercase, digits


def gen_ext(ext: str, name_len_min: int = 6, name_len_max: int = 30, bytes_min: int = 256, bytes_max: int = 4096,
            num_files: int = 10) -> None:
    """
    Генерирует файлы с указанным расширением и случайными именами и данными.

    :Аргументы:
        - ext (str): Расширение файлов, которое будет добавлено к именам сгенерированных файлов.
        - name_len_min (int): Минимальная длина имени файла (количество символов).
        - name_len_max (int): Максимальная длина имени файла (количество символов).
        - bytes_min (int): Минимальное количество байт данных, которые будут записаны в каждый файл.
        - bytes_max (int): Максимальное количество байт данных, которые будут записаны в каждый файл.
        - num_files (int): Количество файлов, которые будут сгенерированы.

    :Возвращаемое значение:
        - None: Функция не возвращает явно заданного значения. Генерирует файлы с указанным расширением и данными.

    :Примечания:
        - Если аргументы name_len_min и name_len_max не указаны, используются значения по умолчанию (6 и 30 соответственно).
        - Если аргументы bytes_min и bytes_max не указаны, используются значения по умолчанию (256 и 4096 соответственно).
        - Если аргумент num_files не указан, используется значение по умолчанию (10).
    """

    for _ in range(num_files):
        name: str = ''.join(choices(ascii_lowercase + digits + '_', k=randint(name_len_min, name_len_max)))
        data: bytes = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)
