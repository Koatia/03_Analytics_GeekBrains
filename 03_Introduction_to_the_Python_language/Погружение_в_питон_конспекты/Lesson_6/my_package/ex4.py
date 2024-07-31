from typing import List, Union

def guessing(text: str, possible_answers: List[str], attempts: int) -> Union[int, None]:

    """
    Функция для угадывания загадки.

    :Аргументы:
        - text (str): Текст загадки.
        - possible_answers (List[str]): Список возможных ответов на загадку.
        - attempts (int): Максимальное количество попыток угадать загадку.

    :Возвращаемое значение:
        - Union[int, None]: Количество попыток, за которое была угадана загадка.
                            Если загадка не была угадана за указанное количество попыток, возвращается None.
    """

    print(f'Необходимо отгадать загадку: {text}\n')

    for attempt in range(1, attempts + 1):
        user_answer: str = input(f'Попытка № {attempt}. Ваш вариант ответа: ')

        if user_answer in possible_answers:
            print(f'\nЗагадка отгадана за {attempt} попытки!\n')
            return attempt

    print(f'\nВы не смогли угадать за {attempts} попытки!\n')
    return 0

__all__ = ['guessing']
