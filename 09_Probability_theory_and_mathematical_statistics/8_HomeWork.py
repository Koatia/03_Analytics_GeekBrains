# Урок 7. Непараметрические тесты

# %%
"""
Задание 1

Найдите ковариацию этих двух величин с помощью элементарных действий,
а затем с помощью функции cov из numpy Полученные значения должны быть равны.

Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных
отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.
"""

import numpy as np
import pandas as pd

# Данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Средние значения
mean_zp = np.mean(zp)
print(mean_zp)

mean_ks = np.mean(ks)
print(mean_ks)

# Ковариация вручную
cov_manual = np.sum((zp - mean_zp) * (ks - mean_ks)) / len(zp)

# Ковариация с использованием numpy
cov_numpy = np.cov(zp, ks, ddof=0)[0, 1]

print(cov_manual, cov_numpy)


# Коэффициент корреляции Пирсона вручную
std_zp = np.std(zp)
print(std_zp)
std_ks = np.std(ks)
print(std_ks)

pearson_manual = cov_manual / (std_zp * std_ks)

# Коэффициент корреляции Пирсона с использованием numpy
pearson_numpy = np.corrcoef(zp, ks)[0, 1]

# Коэффициент корреляции Пирсона с использованием pandas
# Создание DataFrame
df = pd.DataFrame({"zp": zp, "ks": ks})
pearson_pandas = df.corr().loc["zp", "ks"]

print(pearson_manual, pearson_numpy, pearson_pandas)

# %%
"""
Задание 2

Измерены значения IQ выборки студентов, обучающихся в местных технических вузах:
131, 125, 115, 122, 131, 115, 107, 99, 125, 111
Известно, что в генеральной совокупности IQ распределен нормально.
Найдите доверительный интервал для математического ожидания с надежностью 0.95
"""

import numpy as np
from scipy.stats import t

# Данные выборки
IQ = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

# Выборочное среднее и стандартное отклонение
mean_IQ = np.mean(IQ)
std_IQ = np.std(IQ, ddof=1)

# Размер выборки
n = len(IQ)

# Уровень надежности
confidence_level = 0.95
alpha = 1 - confidence_level

# Критическое значение t для 9 степеней свободы
t_critical = t.ppf(1 - alpha / 2, df=n - 1)

# Стандартная ошибка среднего
SE = std_IQ / np.sqrt(n)

# Доверительный интервал
confidence_interval = (mean_IQ - t_critical * SE, mean_IQ + t_critical * SE)

print(mean_IQ, std_IQ, t_critical, SE, confidence_interval)
