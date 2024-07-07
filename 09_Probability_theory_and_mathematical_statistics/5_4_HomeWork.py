import numpy as np
from scipy import stats

# Данные
mothers = np.array([172, 177, 158, 178, 175, 164, 160, 169, 165])
daughters = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])

# Вычисление разностей
differences = mothers - daughters

# Среднее значение разностей
mean_diff = np.mean(differences)

# Стандартное отклонение разностей
std_diff = np.std(differences, ddof=1)

# Количество наблюдений
n = len(differences)

# t-статистика
t_stat = mean_diff / (std_diff / np.sqrt(n))

# Критическое значение для двустороннего теста с уровнем значимости 0.05 и 8 степенями свободы
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)

# p-значение
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))

print(t_stat, t_critical, p_value)
