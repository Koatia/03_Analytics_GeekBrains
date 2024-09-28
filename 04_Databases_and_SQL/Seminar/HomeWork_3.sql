/*
Имеется таблица (сущность) с персоналом staff.
У сущности имеются следующие поля(атрибуты):
id – идентификатор;
firstname – имя;
lastname - фамилия.
post - должность,
seniority – стаж;
salary – заработная плата;
age - возраст.
*/

-- Вы работаете с MySQL
-- Введите свой код ниже

-- 1. Необходимо вывести идентификатор, имя, фамилию, заработную плату из сущности staff. 
-- при этом данные должны быть отсортированы в порядке возрастания заработной платы.

SELECT id, firstname, lastname, salary
FROM staff
ORDER BY salary;

-- 2. Необходимо вывести идентификатор, имя, фамилию, заработную плату из сущности staff
-- при этом данные должны быть отсортированы в порядке убывания заработной платы.

SELECT id, firstname, lastname, salary
FROM staff
ORDER BY salary DESC;

-- 3. Необходимо вывести идентификатор, имя, фамилию, заработную плату
-- пяти самых высокооплачиваемых сотрудников из сущности staff.

SELECT id, firstname, lastname, salary
FROM staff
ORDER BY salary DESC
LIMIT 5;

-- 4. Посчитайте и выведите суммарную зарплату (salary) по каждой специальности (роst) из сущности staff.
-- Порядок вывода атрибутов: должность, суммарная зарплата.

SELECT post, SUM(salary)
FROM staff
GROUP BY post;

-- 5. Посчитайте и выведите количество сотрудников с должностью 'Рабочий' и возрастом не моложе 24 лет и не старше 49 лет.

SELECT COUNT(*)
FROM staff
WHERE age >= 24
AND age <= 49
AND post = 'Рабочий';

-- 6. Найдите средний возраст сотрудников по каждой должности из сущности staff.
-- Выведите только те должности, у которых средний возраст меньше 30 лет.

SELECT post
FROM staff
GROUP BY post
HAVING AVG(age) < 30;
