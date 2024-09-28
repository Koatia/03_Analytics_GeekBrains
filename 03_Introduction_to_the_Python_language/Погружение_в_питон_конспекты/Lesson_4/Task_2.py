# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.


def unique_unicode_codes(text: str) -> list[int]:
    unique_codes: list[int] = sorted(set(map(ord, text)), reverse=True)
    return unique_codes

def __main() -> None:
    text: str = "Hello, World!"
    result: list[int] = unique_unicode_codes(text)
    print(result)

if __name__ == '__main__':
    __main()
