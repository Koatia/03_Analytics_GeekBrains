/*
СДАВАТЬ ссылкой на github с SQL файлом. ИЛИ ворд/пдф, где будет код + скрин результата. НЕ СДАВАТЬ АРХИВ
Вторую задачу решать через процедуру

Задача 1. Создайте функцию, которая принимает кол-во сек и формат их в кол-во дней часов.
Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds '
*/

DELIMITER $$
DROP FUNCTION IF EXISTS format_seconds;
CREATE FUNCTION format_seconds(seconds INT) 
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE days INT;
    DECLARE hours INT;
    DECLARE minutes INT;
    DECLARE remaining_seconds INT;
    DECLARE result VARCHAR(255);

    SET days = FLOOR(seconds / 86400);
    SET seconds = seconds % 86400;
    SET hours = FLOOR(seconds / 3600);
    SET seconds = seconds % 3600;
    SET minutes = FLOOR(seconds / 60);
    SET remaining_seconds = seconds % 60;

    SET result = CONCAT(days, ' days ', hours, ' hours ', minutes, ' minutes ', remaining_seconds, ' seconds');

    RETURN result;
END $$
DELIMITER ;

SELECT format_seconds(1234456) AS formatted_time;

-- # formatted_time
-- '14 days 6 hours 54 minutes 16 seconds'




/*
Задача 2. Выведите только чётные числа от 1 до 10.
Пример: 2,4,6,8,10
*/

DELIMITER $$
DROP PROCEDURE IF EXISTS print_even_numbers;
CREATE PROCEDURE print_even_numbers(IN max_num INT)
BEGIN
    DECLARE num INT DEFAULT 1;
    DECLARE result VARCHAR(255) DEFAULT '';
    WHILE num <= max_num DO
        IF num % 2 = 0 THEN
            SET result = CONCAT(result, num, ',');
        END IF;
        SET num = num + 1;
    END WHILE;
    -- Удаляем последнюю запятую
    SET result = TRIM(TRAILING ',' FROM result);
    SELECT result;
END $$
DELIMITER ;

CALL print_even_numbers(10);

-- # result
-- '2,4,6,8,10'