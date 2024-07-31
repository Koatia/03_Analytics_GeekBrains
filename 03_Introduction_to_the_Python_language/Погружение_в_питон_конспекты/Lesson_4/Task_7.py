# Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# Функция вычисления итоговой прибыли или убытка каждой компании
def calculation_net_profit(company_data: dict[str, list[int]]) -> bool:
    for _, values in company_data.items():
        total_profit: int = sum(values)
        if total_profit < 0:
            return False
    return True


def __main() -> None:
    company_data: dict[str, list[int]] = {
        "Первая компания": [100, 200, 300, -400, -100],
        "Вторая компания": [100, -400, 300, -200, 200],
        "Третья компания": [100, 200, -300, 400, -500]
    }

    result: bool = calculation_net_profit(company_data)
    print(result)

if __name__ == '__main__':
    __main()
