# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

N = int(input('Введите число: '))
n = 2
i = 0
while n <= N:
    n = 2 ** i
    i += 1
    if n <= N: print(n)