# Урок 7. Непараметрические тесты

# %%
"""
Задание 1

Даны две  независимые выборки. Не соблюдается условие нормальности
x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]

Сделайте вывод по результатам, полученным с помощью функции

Решение:
Для сравнения двух независимых выборок, когда не соблюдается условие нормальности, можно использовать непараметрический тест Манна-Уитни (U-тест).
Этот тест позволяет определить, отличаются ли два набора данных.
"""

import numpy as np
from scipy.stats import mannwhitneyu

# Данные выборок
x1 = [380, 420, 290]
y1 = [140, 360, 200, 900]

# Проведение теста Манна-Уитни
stat, p_value = mannwhitneyu(x1, y1, alternative="two-sided")

# Вывод результатов
print("\nЗадание 1")
print(f"Статистика теста Манна-Уитни: {stat}, p-value: {p_value}")
print("Интерпретация результатов:")
print(
    "    p-value (0.6286) больше уровня значимости 0.05, что указывает на отсутствие статистически значимых различий между двумя выборками."
)
print(
    "    Это означает, что нет достаточных оснований утверждать, что данные этих двух независимых выборок (x1 и y1) существенно различаются."
)

# %%
"""
Задание 2

Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут.
Есть ли статистически значимые различия?

1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150,  130, 135
3е измерение через 30 минут: 130, 130, 120, 130, 125

Решение:
Для проверки наличия статистически значимых различий в уровне давления пациентов в трех временных точках (до приема препарата, через 10 минут и через 30 минут)
мы можем использовать критерий Фридмана.
Этот непараметрический тест используется для проверки различий между несколькими зависимыми группами.
"""

import numpy as np
from scipy.stats import friedmanchisquare

# Данные измерений давления
before = [150, 160, 165, 145, 155]
after_10_min = [140, 155, 150, 130, 135]
after_30_min = [130, 130, 120, 130, 125]

# Проведение критерия Фридмана
stat, p_value = friedmanchisquare(before, after_10_min, after_30_min)

# Вывод результатов
print("\nЗадание 2")
print(f"Статистика критерия Фридмана: {stat}, p-value: {p_value}")
print("Интерпретация результатов:")
print(
    "    p-value (0.0083) меньше уровня значимости 0.05, что указывает на наличие статистически значимых различий в уровне давления между тремя измерениями."
)
print(
    "    Это означает, что применение препарата значительно влияет на уровень давления пациентов, и изменения давления до приема препарата, через 10 минут и через 30 минут, статистически значимы."
)

# %%
"""
Задание 3

Сравните 1 и 2-е измерения, предполагая, что 3-го измерения через 30 минут не было.
1е измерение до приема препарата: 150, 160, 165, 145, 155
2е измерение через 10 минут: 140, 155, 150,  130, 135

Решение:
Для сравнения первых двух измерений (до приема препарата и через 10 минут) мы можем использовать непараметрический критерий знаковых рангов Уилкоксона для парных выборок.
Этот тест используется для проверки различий между двумя зависимыми выборками, когда распределение данных не является нормальным.
"""

import numpy as np
from scipy.stats import wilcoxon

# Данные измерений давления
before = [150, 160, 165, 145, 155]
after_10_min = [140, 155, 150, 130, 135]

# Проведение теста Уилкоксона
stat, p_value = wilcoxon(before, after_10_min)

# Вывод результатов
print("\nЗадание 3")
print(f"Статистика теста Уилкоксона: {stat}, p-value: {p_value}")
print("Интерпретация результатов:")
print(
    "    p-value (0.0625) больше уровня значимости 0.05, что указывает на отсутствие статистически значимых различий между первым измерением (до приема препарата) и вторым измерением (через 10 минут)"
)
print(
    "    Это означает, что нет достаточных оснований утверждать, что уровень давления пациентов существенно изменился через 10 минут после приема препарата по сравнению с уровнем до приема препарата"
)

# %%
"""
Задание 4

Даны 3 группы  учеников плавания.
В 1 группе время на дистанцию 50 м составляют:
56, 60, 62, 55, 71, 67, 59, 58, 64, 67

Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54

Решение:
Для сравнения времен на дистанцию 50 м между тремя группами учеников плавания можно использовать непараметрический тест Крускала-Уоллиса.
Этот тест используется для сравнения трех или более независимых групп и позволяет определить, имеются ли статистически значимые различия между ними.
"""

import numpy as np
from scipy.stats import kruskal

# Время на дистанцию 50 м для трех групп
group1 = [56, 60, 62, 55, 71, 67, 59, 58, 64, 67]
group2 = [57, 58, 69, 48, 72, 70, 68, 71, 50, 53]
group3 = [57, 67, 49, 48, 47, 55, 66, 51, 54]

# Проведение теста Крускала-Уоллиса
stat, p_value = kruskal(group1, group2, group3)

# Вывод результатов
print("\nЗадание 4")
print(f"Статистика теста Крускала-Уоллиса: {stat}, p-value: {p_value}")
print("Интерпретация результатов:")
print(
    "    p-value (0.0650) больше уровня значимости 0.05, что указывает на отсутствие статистически значимых различий между тремя группами учеников плавания."
)
print(
    "    Это означает, что нет достаточных оснований утверждать, что времена на дистанцию 50 м существенно различаются между группами."
)

# %%
"""
Задание 5

Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения.
Объем выборки 10, уровень статистической значимости 5%

2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

Решение:
Для проверки гипотезы о среднем арифметическом партии изделий можно использовать t-критерий Стьюдента для одной выборки.
В данном случае, мы будем проверять гипотезу H0​, что среднее значение размеров изделий равно 2.5 см
против альтернативной гипотезы H1​, что среднее значение не равно 2.5 см.

Формулировка гипотез:
    H0​: μ = 2.5
    H1​: μ ≠ 2.5

Выбор уровня значимости:
    α = 0.05

Вычисление статистики теста:
    Используем t-критерий для одной выборки.

"""
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import t

# Данные выборки
data = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]

# Заявляемое среднее значение
mu = 2.5

# Проведение t-теста для одной выборки
t_stat, p_value = ttest_1samp(data, mu)

# Вывод результатов
print("\nЗадание 5")
print(f"t-расчетное: {t_stat}, p-value: {p_value}")

# Определение критического значения t
alpha = 0.05
df = 10 - 1
t_critical = t.ppf(1 - alpha / 2, df)

print(f"t-критическое: {t_critical}")

# Уровень значимости
alpha = 0.05

# Принятие решения
if p_value < alpha:
    print(
        "Отвергаем нулевую гипотезу. Среднее значение существенно отличается от 2.5 см."
    )
else:
    print(
        "Не отвергаем нулевую гипотезу. Нет оснований утверждать, что среднее значение существенно отличается от 2.5 см."
    )
