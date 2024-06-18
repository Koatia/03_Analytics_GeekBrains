# Найдите выручку компании в зависимости от месяца Для этого напишите функцию calc_income_by_month(),
# которая на вход принимает список с датами и список с выручкой,
# а на выходе словарь, где ключи - это месяцы, а значения - это выручка.
# Используйте аннотирование типов.

from typing import List, Dict


def calc_income_by_month(dates: List[str], incomes: List[int]) -> Dict[str, int]:
    income_by_month = {}
    for date, income in zip(dates, incomes):
        # Извлекаем месяц и год из даты
        month = date[5:7]  # Получаем подстроку в формате 'MM'
        # Суммируем выручку по месяцам
        if month in income_by_month:
            income_by_month[month] += income
        else:
            income_by_month[month] = income
    return income_by_month


# Пример использования функции
# dates = ['2021-11-01', '2021-12-01', '2021-11-15']
# incomes = [100, 200, 300]
#
# print(calc_income_by_month(dates, incomes))

print(calc_income_by_month(dates=['2021-11-01'], incomes=[100]))
