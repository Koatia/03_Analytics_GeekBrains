# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# - После каждого ввода добавляйте новую информацию в JSON файл.
# - Пользователи группируются по уровню доступа.
# - Идентификатор пользователя выступает ключём для имени.
# - Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# - При перезапуске функции уже записанные в файл данные должны сохраняться.

from Lesson_8.lesson8_package import add_user_to_json


def main() -> None:
    add_user_to_json('Task_2.json')


if __name__ == "__main__":
    main()
