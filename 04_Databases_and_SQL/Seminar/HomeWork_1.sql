/*
Создайте таблицу (сущность) с мобильными телефонами mobile_phones. При создании необходимо использовать DDL-команды.
Перечень полей (атрибутов):
id – числовой тип, автоинкремент, первичный ключ;
product_name – строковый тип, обязательный к заполнению;
manufacturer – строковый тип, обязательный к заполнению;
product_count – числовой тип, беззнаковый;
price – числовой тип, беззнаковый.
Используя CRUD-операцию INSERT, наполните сущность mobile_phones
*/

-- Название вашей схемы - itresume10019400
-- Например, itresume10019400.tablename

DROP TABLE IF EXISTS itresume10019400.mobile_phones;
CREATE TABLE itresume10019400.mobile_phones (
 id SERIAL PRIMARY KEY,
 product_name VARCHAR(255) NOT NULL,
 manufacturer VARCHAR(255) NOT NULL,
 product_count INT CHECK (product_count >= 0),
 price INT CHECK (product_count >= 0)
);

INSERT INTO itresume10019400.mobile_phones (product_name, manufacturer, product_count, price)
VALUES ('iPhone X', 'Apple', 156, 76000),
 ('iPhone 8', 'Apple', 180, 51000),
 ('Galaxy S9', 'Samsung', 21, 56000),
 ('Galaxy S8', 'Samsung', 124, 41000),
 ('P20 Pro', 'Huawei', 341, 36000);
 
 SELECT * FROM itresume10019400.mobile_phones;
 
 /*
Имеется таблица (сущность) с мобильными телефонами mobile_phones.
У сущности имеются следующие поля(атрибуты):
id – идентификатор;
product_name – название;
manufacturer – производитель;
product_count – количество;
price – цена.
Необходимо вывести название, производителя и цену для мобильных телефонов, у которых количество больше чем 2.
*/

-- Вы работаете MySQL

SELECT 
    product_name, manufacturer, price
FROM
    mobile_phones
WHERE
    product_count > 2;
    
    
/*
Имеется таблица (сущность) с мобильными телефонами mobile_phones.
У сущности имеются следующие поля(атрибуты):
id – идентификатор;
product_name – название;
manufacturer – производитель;
product_count – количество;
price – цена.
Необходимо вывести идентификатор, название, производителя, количество и цену для мобильных телефонов, у которых производитель «Samsung».
*/

-- Вы работаете MySQL

SELECT 
    *
FROM
    mobile_phones
WHERE
    manufacturer = 'Samsung';