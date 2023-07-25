# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

str = tuple(input('Введите буквы через пробел: ').split())
s = list(str)
m = set(str)
for j in m:
    n = 0
    for i in range(len(str)):
        if j == str[i] and n == 0:            
            n += 1
        elif j == str[i] and n >= 1:
            s[i] = f'{str[i]}_{n}'
            n += 1
print(*s)


# str = input('Введите строку: ').split()
# result = {}
# for i in str:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1