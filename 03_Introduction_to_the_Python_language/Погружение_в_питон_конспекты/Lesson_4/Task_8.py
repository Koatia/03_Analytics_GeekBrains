# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце

from typing import Any


# Функция замены содержимого переменных оканчивающихся на s
def replace_variables(arrays: list[int], conditions: tuple[int, int], loops: float, s: str) -> None:
    local_vars: dict[str, Any] = locals()
    new_vars: dict[str, Any] = {}

    for var_name, var_value in local_vars.items():
        if var_name.endswith('s') and var_name != 's' and len(var_name) > 1:
            new_vars[var_name.rstrip('s')] = var_value
            new_vars[var_name] = None

    local_vars.update(new_vars)

    for var_name, var_value in local_vars.items():
        print(f"{var_name}: {var_value}")


def __main() -> None:
    arrays: list[int] = [1, 2, 3]
    conditions: tuple[int, int] = (4, 5)
    loops: float = 6.78
    s: str = "Hello"

    replace_variables(arrays, conditions, loops, s)


if __name__ == '__main__':
    __main()
