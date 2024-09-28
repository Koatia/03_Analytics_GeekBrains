### [Урок 5. Тестирование гипотез](https://gb.ru/lessons/447657)

#### Интерпретация результатов

- **t-статистика (t-statistic):** Если t-статистика меньше критического значения t при заданном уровне значимости, то мы принимаем альтернативную гипотезу.
- **p-значение (p-value):** Если p-значение меньше уровня значимости $\alpha$, то мы принимаем альтернативную гипотезу.

Для проведения парного t-теста вручную, нужно выполнить следующие шаги:

- Вычислить разности между парами значений:

  $d_i = x_i - y_i$

- Найти среднее значение разностей (d):

  $\bar{d} = \frac{1}{n} \sum_{i=1}^n d_i$

- Найти стандартное отклонение разностей (s):

  $s = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (d_i - \bar{d})^2}$

- Вычислить t-статистику:

  $t = \frac{\bar{d}}{s / \sqrt{n}}$

#### Задание 1

Ниже приведены данные из исследования Фреба и Уайта, посвященному исследованию состоянию легких. Мы возьмем данные для группы людей, которые работали в накуренном помещении и для людей, выкуривающих небольшое число сигарет в день. Объемы выборок одинаковые – по 200 человек. Для людей, работающих в накуренном помещении средняя скорость средины выдоха составляет 2,72, std = 0.71, а выкуривающих небольшое число сигарет 2,63, std = 0.73.Можно ли считать одинаковой максимальную объемную скорость середины выдоха одинаковой в обеих группах?

> $H_0: \quad \mu_1=\mu_2; \quad H_1: \quad \mu_1 \neq \mu_2; \quad n_1=n_2=200$
>
> Так как значение $\alpha$ не дано, берем $\alpha=0.05$
>
> $t_p=\frac{\mu_1-\mu_2}{\sqrt{\frac{std_1^2}{n_1}+\frac{std_2^2}{n_2}}}$
>
> t-расчетное $t_p=1.25$
>
> Степень свободы $df=2×(n-1)$
>
> $df = 2×(200-1) = 398$
>
> t-критическое находится по таблице на основе $df \quad и \quad \alpha$
>
> $t_{кр}$ по таблице $=1.96$

**Так как `t-расчетное` $t_p=1.25$ меньше, чем `t-критическое` $t_{кр}=1.96$, то мы принимаем альтернативную гипотезу**

#### Задание 2

Утверждается, что средний рост мужчин национальности Х 179,5. Была взята выборка из 100 человек, по которой получилось среднее арифметическое 178,5. Проверить это утверждение с помощью одностороннего
теста, если известно, что стандартное отклонение генеральной совокупности 3 см. А уровень статистической значимости принять за 1%

> $z_p=\frac{X-\mu}{se}; \quad \text{Стандартная ошибка среднего } se=\frac{\sigma}{\sqrt{n}}$
>
> $\alpha=0.01; \quad se=\frac{3}{\sqrt{100}}=0.3; \quad z_p=\frac{178.5-179.5}{0.3}≈-3.33$
>
> $z_{кр}$ ищем в таблице по значению уровня статистической значимости $\alpha=0.01; \quad z_{кр}=-2.33$

**Так как `z-расчетное` $z_p=-3.33$ меньше, чем `z-критическое` $z_{кр}=-2.33$, то мы принимаем альтернативную гипотезу**