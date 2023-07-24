# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод: ноутбук   Вывод:   12


u = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
u.setdefault('K', 5)
u1 = dict.fromkeys(['D', 'G'], 2)
u2 = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
u3 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4)
u4 = dict.fromkeys(['J', 'X'], 8)
u5 = dict.fromkeys(['Q', 'Z'], 10)
usa = {**u, **u1, **u2, **u3, **u4, **u5}
# print(usa)

str = "А, В, Е, И, Н, О, Р, С, Т".split(", ")
# print(str)
r = dict.fromkeys(str, 1)
# print(r)

str = "Д, К, Л, М, П, У".split(", ")
r1 = dict.fromkeys(str, 2)
str = "Б, Г, Ё, Ь, Я".split(", ")
r2 = dict.fromkeys(str, 3)
str = "Й, Ы".split(", ")
r3 = dict.fromkeys(str, 4)
str = "Ж, З, Х, Ц, Ч".split(", ")
r4 = dict.fromkeys(str, 5)
str = "Ш, Э, Ю".split(", ")
r5 = dict.fromkeys(str, 8)
str = "Ф, Щ, Ъ".split(", ")
r6 = dict.fromkeys(str, 10)
ru = {**r, **r1, **r2, **r3, **r4, **r5, **r6}
# print(ru)

str = input('Введите слово: ')
str = str.upper()
# print(str)

res = 0
for i in range(len(str)):
    if ord('A') == 65:
        p = usa.get(str[i])
        res += int(p)
    else:
        p = ru.get(str[i])
        res += int(p)
print(res)


    
