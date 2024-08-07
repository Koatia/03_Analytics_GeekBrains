### [Урок 6. Сравнение долей. Построение доверительного интервала](https://gb.ru/lessons/447658)

#### Интерпретация результатов

Стандартная ошибка среднего:

$se= \frac{std}{\sqrt{n}}$

Стандартная ошибка разницы средних значений:

$se= \frac{std^2_1}{n_1} + \frac{std^2_2}{n_2}$

$t_{расчетное}=\frac{X_1 - X_2}{se}$

Степень свободы:

$df = n_1+n_2-2$

#### Задание 1

С помощью 90% доверительного интервала оценить средний вес нормально
распределенной популяции, если дисперсия генеральной совокупности 3.6, а среднее
арифметичекое по выборке объемом 100 получилось равным 71.2

Дано:

> $\alpha = 1-0.9 = 0.1$
>
> $D = 3.6$
>
> $\bar{x} = 71.2$
>
> $n = 100$

$\bar{x} \pm z_{\alpha/2} se$

> $1-\frac{0.1}{2} = 0.95; \quad \text{по таблице } z_{\alpha/2} = 1.65$

Подставляем значения и находим доверительный интервал

> $71.2 \pm 1.65 × \frac{\sqrt{3.6}}{\sqrt{100}}; \quad (70.9; 71.5)$

Ответ: У всей генеральной совокупности с вероятностью 90% среднее значение веса будет находиться в этом диапазоне
