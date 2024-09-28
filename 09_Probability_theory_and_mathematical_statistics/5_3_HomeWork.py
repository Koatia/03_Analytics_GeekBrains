import numpy as np
from scipy import stats

# Данные
x = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
mu = 200  # Средний вес по утверждению продавца

# Выборочное среднее
mean_x = np.mean(x)
print(mean_x)

# Выборочное стандартное отклонение
std_x = np.std(x, ddof=1)
print(std_x)

# Количество наблюдений
n = len(x)

# t-статистика
t_stat = (mean_x - mu) / (std_x / np.sqrt(n))

# Критическое значение для двустороннего теста с уровнем значимости 0.01 и 9 степенями свободы
alpha = 0.01
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)

# p-значение
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))

print(t_stat, t_critical, p_value)
