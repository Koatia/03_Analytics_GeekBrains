/*
Задача 1
Создание справочника

Имеется таблица (сущность) с мобильными телефонами mobile_phones.
У сущности имеются следующие поля(атрибуты):
id – идентификатор;
product_name – название;
manufacturer – производитель;
product_count – количество;
price – цена.

Сущность mobile_phones имеет следующие записи:
 | id | product_name | manufacturer | product_count | price |
 | --- | ------------ | ------------ | ------------- | ----- |
 | 1 | iPhone X | Apple | 156 | 76000 |
 | 2 | iPhone 8 | Apple | 180 | 51000 |
 | 3 | Galaxy S9 | Samsung | 21 | 56000 |
 | 4 | Galaxy S8 | Samsung | 124 | 41000 |
 | 5 | P20 Pro | Huawei | 341 | 36000 |

Создайте таблицу (сущность) с заказами manufacturer. При создании необходимо использовать DDL-команды.
Перечень полей (атрибутов):
id – числовой тип, автоинкремент, первичный ключ;
name – строковый тип;

Используя CRUD-операцию INSERT, наполните сущность manufacturer в соответствии с данными, имеющимися в атрибуте manufacturer сущности mobile_phones.
*/

-- При написании запросов указывайте не только имя таблицы, но и схему.
-- Название вашей схемы - itresume10019400

-- Вы работаете с PostgreSQL


DROP TABLE IF EXISTS itresume10019400.manufacturer;
CREATE TABLE itresume10019400.manufacturer (
	id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO itresume10019400.manufacturer 
SELECT id, product_name
FROM itresume10019400.mobile_phones;

SELECT * from itresume10019400.manufacturer;

/*
Задача 2
Вывод статуса количества мобильных телефонов

Имеется таблица (сущность) с мобильными телефонами mobile_phones.
У сущности имеются следующие поля(атрибуты):
id – идентификатор;
product_name – название;
manufacturer – производитель;
product_count – количество;
price – цена.

Сущность mobile_phones имеет следующие записи:

id	product_name	manufacturer	product_count	price
1	iPhone X	Apple	156	76000
2	iPhone 8	Apple	180	51000
3	Galaxy S9	Samsung	21	56000
4	Galaxy S8	Samsung	124	41000
5	P20 Pro	Huawei	341	36000
Статусы количества мобильных телефонов (в зависимости от количества): меньше 100 – «little»; от 100 до 300 – «many»; больше 300 – «lots».

Необходимо вывести название, производителя и статус количества для мобильных телефонов.
*/
-- Вы работаете с MySQL

SELECT product_name, manufacturer,
CASE 
	WHEN product_count >= 300 THEN 'lots'
    WHEN product_count >= 100 THEN 'many'
    ELSE 'little'
END AS status_count
FROM mobile_phones;

/*
Задача 3
Создание внешнего ключа

Имеется таблица (сущность) с мобильными телефонами mobile_phones.
У сущности имеются следующие поля(атрибуты):
id – идентификатор;
product_name – название;
manufacturer – производитель;
product_count – количество;
price – цена.

Сущность mobile_phones имеет следующие записи:
id	product_name	manufacturer	product_count	price
1	iPhone X	Apple	156	76000
2	iPhone 8	Apple	180	51000
3	Galaxy S9	Samsung	21	56000
4	Galaxy S8	Samsung	124	41000
5	P20 Pro	Huawei	341	36000
Имеется таблица-справочник (сущность) производителей manufacturer.
У сущности имеются следующие поля(атрибуты):
id – идентификатор;
name – название.

Сущность manufacturer имеет следующие записи:
id	name
1	Apple
2	Samsung
3	Huawei

1. Создайте для сущности mobile_phones внешний ключ manufacturer_id (идентификатор производителя),
направленный на атрибут id сущности manufacturer. Установите каскадное обновление - CASCADE,
а при удалении записи из сущности manufacturer – SET NULL.
2. Используя CRUD-операцию UPDATE обновите данные в атрибуте manufacturer_id сущности mobile_phones согласно значений, имеющихся в атрибуте manufacturer.
3. Удалите атрибут manufacturer из сущности mobile_phones.
4. Выведите идентификатор, название и идентификатор производителя сущности mobile_phones.
*/
-- При написании запросов указывайте не только имя таблицы, но и схему.
-- Название вашей схемы - itresume10019400
-- Вы работаете с PostgreSQL

-- # вывод инфо о таблице
-- SELECT column_name, column_default, data_type 
-- FROM INFORMATION_SCHEMA.COLUMNS 
-- WHERE table_name = 'mobile_phones';

-- # удаляю столбец после неудачного создания ключа
-- ALTER TABLE itresume10019400.mobile_phones
-- DROP COLUMN manufacturer_id; 

-- 1
ALTER TABLE itresume10019400.mobile_phones
ADD COLUMN manufacturer_id INT,
ADD CONSTRAINT fk_manufacturer_id
    FOREIGN KEY (manufacturer_id)
    REFERENCES itresume10019400.manufacturer(id)
    ON UPDATE CASCADE
    ON DELETE SET NULL;

-- 2
UPDATE itresume10019400.mobile_phones
SET manufacturer_id = (
    SELECT id
    FROM itresume10019400.manufacturer
    WHERE itresume10019400.manufacturer.name = itresume10019400.mobile_phones.manufacturer
);

-- 3
ALTER TABLE itresume10019400.mobile_phones
DROP COLUMN manufacturer;

-- 4
SELECT id, product_name, manufacturer_id
FROM itresume10019400.mobile_phones;


/*
Задача 4
Вывод подробного описания статуса

Имеется таблица (сущность) с заказами orders.
У сущности имеются следующие поля(атрибуты):
id – идентификатор;
mobile_phones_id – идентификатор мобильного телефона;
order_status - статус.

id	mobile_phones_id	order_status
1	1	OPEN
2	1	OPEN
3	1	CLOSED
4	4	OPEN
5	4	CANCELLED
Подробное описание статусов заказа:
OPEN – «Order is in open state» ;
CLOSED - «Order is closed»;
CANCELLED - «Order is cancelled»

Необходимо вывести идентификатор и подробное описание статуса заказа.
*/

SELECT id,
CASE order_status
	WHEN 'OPEN' THEN 'Order is in open state'
    WHEN 'CLOSED' THEN 'Order is closed'
    WHEN 'CANCELLED' THEN 'Order is cancelled'
END AS full_order_status
FROM orders;

