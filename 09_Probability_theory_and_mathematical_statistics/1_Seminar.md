### [Урок 1. Расчет вероятности случайных событий](https://gb.ru/lessons/447653)

![alt text](Формулы_комбинаторики.png)

#### Задание 1

В партии 10 деталей. Среди них 3 бракованные.
Какова вероятность, что среди 5, взятых на удачу, 4 хорошие детали?
> $$ \frac {C^4_{7} \times C^1_{3}} {C^5_{10}} = \frac {\frac {7!}{4! \times (7-4)!} \times 3}{\frac {10!}{5! \times (10-5)!}} = \frac {7! \times 3}{4! \times 3!} \times \frac {5! \times 5!}{10!} = \frac {5}{12} $$

#### Задание 2

Разработали спам-фильтр на основании часто встречающихся фраз. 70% всех писем –это
спам. В 10 % писем со спамом встречается фраза: «вся правда о» и в 0.5% она встречается
в хороших письмах.
Какова вероятность, что пришедшее на почту письмо является спамом,если в нем есть данная фраза?

> $$ \frac {0.7 \times 0.1}{0.7 \times 0.1 + 0.3 \times 0.005} = \frac {7}{7 + 0.15} = 0.97$$

#### Задание 3

В ящике находится 10 красных, 5 черных, 5 зеленых шаров. Наудачу вынимают 6 шаров.
Какова вероятность, что вынуты 3 красных, 2 черных, 1 зеленый?

> $$ \frac {C^3_{10} \times C^2_{5} \times C^1_{5}} {C^6_{20}} = \frac {50}{323} $$


#### Задание 4

На 5 одинаковых карточках написаны буквы Ч, А, Й ,К, И
Какова вероятность, что получится слова:
- ЧАЙКИ

> $$ \frac {1} {5 \times 4 \times 3 \times 2 \times 1} =  \frac {1} {5!} =  \frac {1} {120} $$
- Ч`А`ЙК`А`

> $$ \frac {1 + 1} {5 \times 4 \times 3 \times 2 \times 1} =  \frac {2} {5!} =  \frac {1} {60} $$

#### Задание 6

Какое количество семизначных номеров можно придумать, если в качестве первой цифры не может быть [0, 1, 7]

> $$ 7 \times 10 \times 10 \times 10 \times 10 \times 10 \times 10 = 7 \times 10^6 $$