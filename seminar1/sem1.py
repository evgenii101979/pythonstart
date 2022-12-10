# квадрат числа

# a=int(input())
# print(a**2)

# программа принимает 2 числа и проверяет является ли одно квадратом другого

# a=int(input('a '))
# b=int(input('b '))
# if a**2==b or b**2==a:
#     print('является')
# else:
#     print('Не является')

# принимает 5 чисел и ищет макс.

# a=input().split()
# print(a)
# max = int(a[0])
# for i in range(len(a)):
#     if int(a[i])>max:
#         max=int(a[i])
# print(max)

# a=list(map(float,input().split()))
# print(max(a))

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n=int(input('n '))
# a=[]
# b=''
# for i in range(-n,n+1):
#     a.append(i)
#     print(f' {i} ', end='')
#     b+=f' {i} '
# print()
# print(a)
# print(b)

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# n=abs(float(input('n ')))
# print(int(n * 10 % 10))

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a=float(input('a '))
if ((a % 5 == 0 and a % 10 == 0) or a % 15 == 0) and a % 30 != 0:
    print("Yes")
else:
    print("No")