def process_files(names_file: str, nums_file: str, result_file: str) -> None:
    """
    Обрабатывает файлы с именами и числами, выполняет операции над данными и записывает результат в выходной файл.

    :Аргументы:
        - names_file (str): Имя файла с именами.
        - nums_file (str): Имя файла с числами.
        - result_file (str): Имя выходного файла, в который будут записаны результаты обработки.

    :Возвращаемое значение:
        - None: Функция не возвращает явно заданного значения. Результаты обработки записываются в выходной файл.

    :Пример записи в выходной файл:
        - kepba 217343.46602478344
        - RIHV 777216
    """

    with open(names_file, 'r', encoding='utf-8') as f_names, \
            open(nums_file, encoding='utf-8') as f_nums, \
            open(result_file, 'w', encoding='utf-8') as f_res:

        data_nums = f_nums.readlines()
        data_names = f_names.readlines()

        for i in range(max(len(data_nums), len(data_names))):
            int_value, float_value = map(float, data_nums[i % len(data_nums)].split('|'))
            name = data_names[i % len(data_names)].strip()

            mult_res = int_value * float_value

            if mult_res < 0:
                res = name.lower() + ' ' + str(abs(mult_res))
            else:
                res = name.upper() + ' ' + str(round(mult_res))

            f_res.write(res + '\n')
