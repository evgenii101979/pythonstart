# 2. Напишите программу, которая принимает на вход 
# число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input("Введите число N: "))
c = list(map(lambda n: (-3)**n, range(n)))
print(c)