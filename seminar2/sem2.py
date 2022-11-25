# '1. Напишите программу, которая принимает на вход 
# число N и выдаёт последовательность из N членов.

# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# n = 5
# for i in range(n):
#     print(f' {(-3)**i} ', end='')

# '2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.

# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Введите число N: "))
# d = {}
# for i in range(1,n+1):
#     d[i] = 3*i + 1
# print(d)

# '3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

a = input()
b = input()
count = 0
for i in range(len(a)):
    if a[i:i+len(b)] == b:
        count += 1
print(count)
print(a.count(b))


# print(compile.__doc__)

