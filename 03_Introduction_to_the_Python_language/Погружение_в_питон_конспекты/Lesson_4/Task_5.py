# Функция принимает на вход три списка одинаковой длины:
# - имена str,
# - ставка int,
# - премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.


# Функция для расчёта суммы премии для каждого имени из списка
def calculate_result(names: list[str], rates: list[int], interest_rate: list[str]) -> dict[str, float]:
    result: dict[str, float] = {names[i]: rates[i] * float(interest_rate[i].strip('%')) / 100 for i in range(len(names))}
    return result

def __main() -> None:
    names: list[str] = ["Name_1", "Name_2", "Name_3"]
    rates: list[int] = [728, 1833, 2971]
    interest_rate: list[str] = ["6.30%", "4.50%", "7.75%"]

    result: dict[str, float] = calculate_result(names, rates, interest_rate)
    print(result)

if __name__ == '__main__':
    __main()
