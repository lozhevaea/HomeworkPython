# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Вам требуется написать программу, 
# которая проверяет счастливость билета с номером n и выводит на экран yes или no.

n = int(input('Введите номер билета: ')) 
s1 = (n//100000 + n//10000%10 + n//1000%10)
s2 = (n//100%10 + n//10%10 + n%10)
if s1 == s2: print('YES')
else: print('NO') 