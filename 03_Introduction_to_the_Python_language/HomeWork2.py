print("\033[H\033[J") # Очистка консоли

"""
На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

Входные данные:
На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

Выходные данные:
Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
"""

coins = [0, 1, 0, 1, 1, 0, 1]

count1 = 0
count2 = 0

for i in coins:
    if i:
        count1 += 1
    else:
        count2 += 1

print(min(count1, count2))


"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

y = s - x
x * (s - x) == p

На входе:
s = 12
p = 27

На выходе:
3 9
"""

s = 12
p = 27

for x in range(1, 1001):
    if (x * (s - x) == p) and (x <= s - x):
        print(x, s - x)

# Второй вариант решения
x = 1
while x < 1000 and (x * (s - x) != p):
    x += 1

print(x, s - x)

"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n=16

#Вывод
1
2
4
8
16
"""

n = 16
res = 1

while res <= n:
    print(res)
    res *= 2
