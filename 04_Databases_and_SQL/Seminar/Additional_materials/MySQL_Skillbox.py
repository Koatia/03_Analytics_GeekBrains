https://code.mu/ru/sql/manual/ # - полезный справочник

1) После оператора GROUP BY должны перечисляться ВСЕ неагрегированные столбцы,
указанные в запросе после SELECT  (то есть столбцы, к которым не применены групповые функции).

2) необходимо учитывать порядок выполнения  SQL запроса на выборку на СЕРВЕРЕ:

MySQL: FROM => WHERE = SELECT = GROUP BY = HAVING = ORDER BY = LIMIT.
PostgreSQL: FROM => WHERE = GROUP BY = HAVING = SELECT = DISTINCT = ORDER BY = LIMIT.

3) операторы сравнения- <, >, =, <>

use skillbox; # - использовать базу данных skillbox
show tables; # - показать таблицы
describe courses; # - показать структуру таблицы courses
describe courses\G  # - показать структуру таблицы courses построчно


SELECT name, type FROM courses; # select - выбираем колонки name, type from - из таблицы courses;
SELECT * FROM students\G # - выведет всю информацию из всех колонок \G - построчно

SELECT * FROM courses WHERE type = "PROGRAMMING"; # вы бираем все курсы WHERE - у которых type= "PROGAMMING"
SELECT * FROM students WHERE age > 35; # вы бираем всех студентов WHERE - у которых age > 35
SELECT * FROM teachers WHERE salary > 20000; # вы бираем всех учителей WHERE - у которых salary > 20000
SELECT * FROM teachers WHERE salary > 20000 AND age < 30;
# вы бираем всех учителей WHERE - у которых salary > 20000 AND - и age < 30;
SELECT * FROM teachers WHERE salary BETWEEN 10000 AND 20000;  # выбираем всех учиителей с зарплатой от 10000 до 20000 включительно
SELECT * FROM teachers WHERE salary IN (10000,12000, 17000);  # выбираем всех учиителей с зарплатой (10000,12000, 17000)
SELECT * FROM teachers WHERE name LIKE '%М%';  # выбираем всех учиителей с буквой "М" в середине слова
SELECT * FROM teachers WHERE name LIKE '%______%';  # выбираем всех учиителей с именем из 6 символов
            # % Любая строка, содержащая ноль или более символов
            # _ (подчеркивание) Любой одиночный символ
SELECT * FROM teachers WHERE salary > ANY (SELECT AVG(salary) FROM teachers GROUP BY salary);
            # ANY - хотя бы один из
            # ALL - все из
            # используются только с вложенными запросами в которых есть группировка
SELECT * FROM students ORDER BY age\G # - таблица students ORDER BY - отсортированная по возрасту age
SELECT * FROM students ORDER BY age DESC\G # - таблица students отсортированная по возрасту age DESC -в обратноп порядке
SELECT * FROM teachers ORDER BY age DESC, salary ASC\G
# - таблица teachers  отсортированная сначала по возрасту - age DESC -в обратноп порядке, потом по зарплате в обычном
SELECT * FROM teachers ORDER BY age LIMIT 3; # - таблица teachers отсортированная по возрасту - age по возрастанию
# LIMIT 3 - только первые 3
SELECT name, duration, students_count FROM courses WHERE type="PROGRAMMING" ORDER BY price LIMIT 3; #
# - выведет из таблицы courses столбцы - name, duration, students_count , только с type - "PROGRAMMING",
# LIMIT 3 - только первые 3 по списку, ORDER BY price - отсортированные по цене
SELECT DISTINCT type FROM courses; # - выведет из таблицы courses столбцы - type, DISTINCT - только уникальные значения
SELECT DISTINCT type, duration FROM courses; # - выведет из таблицы courses столбцы - type и duration
# DISTINCT - только уникальные сочетания двух колонок type и duration
(SELECT name FROM students) # - скобки нужны только для более сложных запросов
UNION
(SELECT name FROM teachers); # - выведет объединенную таблицу учеников и учителей students, teachers
SELECT age, name FROM teachers UNION ALL Select age, name FROM studetns; # - выведет объединённые таблицы teachers  и
# students/ ALL Select age, name - без этого модификатора не будут показываться те, кто является  и студентом и учителем.
# UNION работает только при условии одинакового числа колонок, UNION выкидывает все записи дубликатов, которые ему
# попадаются, что бы этого избежать нужно прописать UNION ALL
SELECT salary, salary * 12 FROM teachers LIMIT 10; # - Выведет две колонки  - salary и salary * 12 из таблицы teachers
# LIMIT 10 - первые 10 записей
SELECT salary AS monthly_salary, salary * 12 AS annual_salary FROM teachers LIMIT 10; # -
# AS - сохранить получившуюся колонку salary как monthly_salary и т.д.
SELECT DATEDIFF(NOW(), registration_date) AS days_since_registration FROM students LIMIT 10; #-
# FROM students - из таблицы students, LIMIT 10; - выводит первые 10 результатов
# DATEDIFF(NOW(), registration_date) - находит разницу между NOW()- сегодняшней датой и колонкой
# registration_date - датой регистрации
# AS - сохраняет результат в новую колонкуd ays_since_registration
MONTH('2020-04-12') # - выделяет только месяц из всей записи
MONTHNAME(дата) # -  возвращает название месяца

SELECT name, IF(students_count > 100, "FULL", "NOT FULL")AS status FROM courses LIMIT 10;
# FROM -из таблицы courses LIMIT 10 - берем перевые 10 строк
# SELECT name, - выбираем колонку name - название курса
# IF(students_count > 100, "FULL", "NOT FULL") - если в колонке students_count- количество студентов > 100
# то результат "FULL", в противном случае "NOT FULL"
# AS status - сохраняем результат в новую колонку status
SELECT CONCAT("Please buy our new course '", name , "' it's only", duration, " hours long, and the price as low ",
              price, " rub.") FROM courses  LIMIT 3;
# CONCAT -  соединяет текст и различные ячейки FROM - из таблицы courses  LIMIT 3 - первые 3 строки

        Агрегирующие функции:
SELECT COUNT(*) FROM students; # - COUNT(*) - сосчитает количество (*) - всех строк из таблицы students
SELECT AVG(age) FROM students; # -  AVG(age) - сосчитает AVG() - средний age - возраст из таблицы students
SELECT AVG(duration), MAX(students_count), MAX(price) FROM courses;
# AVG(duration) - среднее duration - продолжительность курса
# MAX(students_count) - максимальное количество студентов на курсе,
# MAX(price) - максимальная цена за курс
SELECT SUM(duration) AS total_duration FROM courses WHERE type = "MARKETING"; # SUM(duration) - сумма всех duration
# из таблиицы courses, только те ячейки, где колонка type - тип = "MARKETING", сохраним как total_duration

        Соединение таблиц:
1) КОГДА ТАБЛИЦЫ ЗАВИСЯТ ДРУГ ОТДРУГА
SELECT price,                                       # ВЫВЕДЕМ ЦЕНУ КУРСА
courses.name AS courses_name,                       # НАЗВАНИЕ КУРСА В КОЛОНКЕ courses_name
teachers.name AS teacher_name                       # ИМЯ УЧИТЕЛЯ В КОЛОНКЕ teacher_name
FROM courses                                        # ИЗ ТАБЛИЦЫ courses
JOIN teachers ON teachers.id = courses.teacher_id   # СОЕДИНЯЕМ С ТАБЛИЦЕЙ teashers СОПОСТАВЛЯЯ teachers.id ИЗ teachers С courses.teachers_id ИЗ courses
WHERE type="MANAGEMENT"                             # ПРИ ЭТОМ БЕРЁМ ТОЛЬКО ТЕ КУРСЫ ГДЕ type="MANAGEMENT"
ORDER BY price LIMIT 4;                             # ОТСОРТИРОВАЛИ ПО ЦЕНЕ, ВЗЯЛИ 4 ПЕРВЫЕ ЗАПИСИ

2) КОГДА ТАБЛИЦЫ ЗАВИСЯТ ДРУГ ОТ ДРУГА ЧЕРЕЗ ТРЕТЬЮ ТАБЛИЦУ  # вывод  courses_name и students_name
SELECT courses.name AS courses_name,                        # ВЫВДЕМ courses.name - НАЗВАНИЕ КУРСА AS - СОХРАНИМ В КОЛОНКУ - courses_name
students.name AS student_name                               # ВЫВДЕМ students.name - ИМЕНА СТУДЕНТОВ AS - СОХРАНИМ В КОЛОНКУ - student_name
FROM courses                                                # ИЗ ТАБЛИЦЫ courses
JOIN subscrtiptions ON courses.id = subscriptions.course_id  # СОЕДИНЯЕМ С ТАБЛИЦЕЙ subsrtiptions СОПОСТАВЛЯЯ courses.id ИЗ courses С subsrtiptions.courses_id ИЗ subsrtiptions
JOIN students ON students.id = subscriptions.student_id     # СОЕДИНЯЕМ С ТАБЛИЦЕЙ students СОПОСТАВЛЯЯ students.id ИЗ students С subsrtiptions.student_id ИЗ subsrtiptions
WHERE type = "DESIGN"                                       # ПРИ ЭТОМ БЕРЁМ ТОЛЬКО ТЕ КУРСЫ ГДЕ type="DESIGN"
ORDER BY subscription_date                                  # ОТСОРТИРОВАВ ПО subscription_date  - ДАТЕ ПОДПИСКИ
LIMIT 10;                                                   # ВЗЯЛИ ПЕРВЫЕ 10 ЗАПИИСЕЙ

        Группировка:
SELECT type, AVG(price) FROM courses GROUP BY type; #  из таблицы courses выбираем колонку type и ищем среднюю по price,
# при этом группируем по колонке type - получаем средние значения по каждой из групп в колонке type
# при группировке обязательно необходимо выполнить аггрегацию - функция,которая объединяет некоторые строки.

SELECT teachers.name AS teacher_name,# выбрать имена учителей и сохранить в столбце teacher_name
COUNT(*) AS course_count FROM courses #  из таблицы courses посчитать количество записей, т.е сколько курсов ведёт данный преподаватель
JOIN teachers ON teachers.id = courses.teacher_id # присоединим таблицу teachers сопостовляя teachers.id с courses.teacher_id
GROUP BY teachers.id # группируем по id учителя
HAVING salary > 5000 # аналог оператора WHERE для сгруппированных колонок
ORDER BY COUNT(*) DESC LIMIT 5; # - отсортировали по количеству курсов по убыванию  и вывел первые 5 позиций

        Модификация данных:
INSERT INTO courses (name, duration, price, teacher_id) VALUES("SQL", 2, 99999, 2); #  (name, duration, price, teacher) - необязательно все стоблцы) мы вставляем значения соответственно
UPDATE courses SET price = 9000 WHERE id = 46; # UPDATE - меняет price на 9000, WHERE - в той строке где id = 46 в таблице courses
UPDATE courses SET price = price * 0.95 WHERE type = "DESIGN"; # UPDATE - Делает price равным 95% от исходного(5% скидка)
# , WHERE - во всех курсах по дизайну - type = "DESIGN"

        Подзапросы:
# для каждого ученика выведет количество учителей, которые старше этого ученика
SELECT name, (SELECT COUNT(*) FROM teachers WHERE teachers.age > students.age) AS older_count
FROM students ORDER BY older_count DESC LIMIT 10;
# ОСНОВНОЙ ЗАПРОС:
# SELECT name, FROM students ORDER BY older_count DESC LIMIT 10;
# SELECT name- взяли имена FROM students - из таблицы students
# ORDER BY - отсортировали по older_count DESC - в обратном порядке LIMIT 10 - вывели первые 10 позиций,
# ПОДЗАПРОС:
# (SELECT COUNT(*) FROM teachers WHERE teachers.age > students.age) AS older_count
# (SELECT COUNT(*)  - сосчитали все строки FROM - из таблицы teachers, WHERE - где возраст учителей
# teachers.age > students.age - больше чем возраст самого студента
# AS - сохранили как older_count

        Создание и изменение структуры данных:
1.1 - вариант
INSERT INTO имя_таблицы(поле1, поле2)
VALUES (значение1, значение2),
       (значение1, значение2); # вставляем в таблицу значения - несколько строк

1.2 - вариант # - вставляем целую таблицу или часть из неё
INSERT INTO имя_таблицы(поле1, поле2)
SELECT ....; # вставляем в таблицу значения - несколько строк

1.3 - вариант # - на основе уже имеющейся таблицы
0) Создаём таблицу на основе уже имеющейся  в одной действие:
CREATE TABLE new_table
  AS (SELECT * FROM old_table);

1)Создаём таблицу с пустыми колонками
CREATE TABLE purchaselist ( # - создаём новую таблицу purchaselist, далее указыываем колонки нашей новой таблицы
    id INT PRIMARY KEY AUTO_INCREMENT, # создаём колонку с id
    student_name VARCHAR(500), # student_name - название VARCHAR(500) - текстовые данные длинной до 500 символов
    course_name VARCHAR(500), #  VARCHAR(500) - текстовые данные длинной до 500 символов
    price INT, #  INT - числовой тип данных
    subscription_date DATETIME); # DATETIME - тип данных дата

1.2) Создаём связную таблицу:

CREATE TABLE book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author_id INT NOT NULL,  # для внешних ключей рекомендуется устанавливать ограничение NOT NULL
    price DECIMAL(8,2),
    FOREIGN KEY (author_id)  REFERENCES author (author_id) ON DELETE CASCADE);
    # FOREIGN KEY (author_id)  - связанный столбец зависимой таблицы
    # REFERENCES author (author_id)  - главная таблица (связанное_поле_главной_таблицы)
    # ON DELETE при удалении строки из главной таблицы в подчиненной таблице:
            # CASCADE: удаляет строки
            # SET NULL: устанавливает для столбца внешнего ключа значение NULL (должен поддерживать NULL)
            # SET DEFAULT устанавливает для столбца внешнего ключа значение по умолчанию для данного столбца.
            # RESTRICT: отклоняет удаление строк.

2) Создаём запрос
SELECT students.name AS student_name,  # выбираем имена студентов сохраняем в колонку student_name
        courses.name AS course_name, # выбираем название курсов сохраняем в колонку course_name
price, subscription_date FROM courses # выбираем price и subscription_date FROM  из таблицы courses

3) Вставляем в таблицу purchaselist прошлый запрос -т.е заполняем нашу пустую таблицу необходимыми данными,
при этом заранее соединив необходимые даные между собой из двух таблиц
INSERT INTO purchaselist(student_name, course_name, subscription_date, price)
SELECT students.name AS student_name,courses.name AS course_name, subscription_date, price FROM courses
JOIN subscriptions ON subscriptions.course_id = courses.id # присоединим таблицу subscriptions сопостовляя subscriptions.course_id c courses.id
JOIN students ON students.id = subscriptions.student_id; # присоединим таблицу students сопостовляя students.id c subscriptions.student_id

4) Удаляем или добавляем колонку к уже существующей
ALTER TABLE courses ADD COLUMN price_per_hour FLOAT; # ALTER TABLE courses - изменяем таблицу courses
# ADD COLUMN price_per_hour FLOAT - добавляя колонку price_per_hour с типом данных FLOAT (изначально она пустая)

UPDATE courses SET  price_per_hour = price/duration # UPDATE обновляем таблицу courses ,
# в колонке price_per_hour добавляем значения использую другие колонки - price/duration
# Здесь нет WHERE так как применяем ко всей таблице, а не в отдельных строках

            Удаление
DELETE FROM таблица WHERE условие; # удаление из(FROM) таблицы, при условии (WHERE)

            Удаление с использованием связных таблиц
DELETE FROM table_1
USING
    table_1
    INNER JOIN table_2 ON table_1.t1_id = table_2.t1_id
WHERE table_1.amount < 3;

            Математические функции
CEILING(x) #    округлеиние вверх до целого числа
ROUND(x, k) # округление по правилам, k - колиичество знаков после запятой, по умолчанию - до целого
FLOOR(x) #  округлеиние вниз до целого числа
POWER(x, y) # возведение x в степень y
SQRT(x) # квадратный корень из x
DEGREES(x)  # переводим значение x из радиан в градусы
RADIANS(x)  # переводим значение x из градусов в радианы
ABS(x)  # модуль числа x
PI() #  pi = 3.1415926...
GREATEST(5, 0) # вернёт наибольшее из этих двух
            Дополнительные функции
RAND() # случайное число
COALESCE(SUM(amount), 0) # вернет 0 если amount = 0 или не нашёл таких строк
DATE_ADD('2023-01-01', INTERVAL 23 unit) # - прибавление числа 23 к дате в зависимости от значения unit:
MICROSECOND/SECOND/MINUTE/HOUR
DAY/WEEK/MONTH/QUARTER/YEAR
SECOND_MICROSECOND
MINUTE_MICROSECOND/MINUTE_SECOND/
HOUR_MICROSECOND/HOUR_SECOND/HOUR_MINUTE
DAY_MICROSECOND/DAY_SECOND/DAY_MINUTE/DAY_HOUR
YEAR_MONTH
            Строчные функции
SUBSTRING("Какая-то любая строка или столбец", 1, 30) # - ограничение по длине строки от 1 до 30 символов
GROUP_CONCAT('любой столбец или строка, можно перечислить через запятую, если несколько столбцов')
# - можно использовать как SUM() со строками при GROUP BY

            # Запросы с несколькими таблицами:
        # для двух таблиц, внутреннее соединение INNER JOIN;
        # для двух таблиц, внешние соединения LEFT JOIN и RIGHT JOIN;
        # для двух таблиц, перекрестное соединение CROSS JOIN;
        # выборки данных из нескольких таблиц;
        # операторы соединения, использование USING.

                Соединение INNER JOIN - для соединения двух таблиц(симметричное)
SELECT * FROM table_1
INNER JOIN table_2 ON table_1.t1_id = table_2.t1_id;

                Внешнее соединение LEFT/RIGHT JOIN(несимметричное) - можно LEFT/RIGHT OUTER JOIN
SELECT * FROM table_1
LEFT JOIN table_2 ON table_1.t1_id = table_2.t1_id;
    # если LEFT JOIN - То, результат формируется из таблицы table_1, если каких то позиций нет в table_2,
    # то такие позиции имеют значения  NULL
    # если RIGHT JOIN - То, результат формируется из таблицы table_2, если каких то позиций нет в table_1,
    # то такие позиции имеют значения  NULL

                Перекрестное соединение CROSS JOIN(симметричное)
SELECT * FROM table_1, table_2;
        # или
SELECT * FROM table_1 CROSS JOIN table_2;

                Запросы на выборку из нескольких таблиц
SELECT * FROM table_1
    INNER JOIN table_2 ON table_1.t1_id = table_2.t1_id
    INNER JOIN table_3 ON table_3.t2_id = table_2.t2_id;

                Операция соединение, использование USING()
USING позволяет указать набор столбцов, которые есть в обеих объединяемых таблицах

SELECT * FROM table_1 INNER JOIN table_2 USING(t1_id, t2_id, t3_id);










