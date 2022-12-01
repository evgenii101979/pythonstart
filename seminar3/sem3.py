# задача 1  Задайте список. Напишите программу,
# которая определит, присутствует ли в заданном списке некое число.

# list1 = ['lklk', -15, 'ff-d-d-d+d', 4, 2.2556]
# print(list1)
# a = ""
# for i in list1:
#     if type(i) == int or type(i) == float:
#         a = 'yes'
#         break
#     else:
#         a = 'no'
# print(a)

# mass = ['ssss', 'sngujn556', 44]
# types = [str(type(i)) for i in mass]
# print(types)
# if "<class 'int'>" in types or "<class 'float'>" in types:
#     print('Yes')
# else:
#     print('No')

# задача 2  Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# mass = ["123", "234", "123", "567"]
# a = "123"

# try:
#     mass.remove(a)
#     print((mass.index(a))+1)
# except ValueError:
#     print(-1)

import math
# def milt(n: int) -> str:
#     """пготтыпт"""
#     str_mult = '1'
#     for i in range(2, n+1):
#         if i == n:
#             str_mult +=f'*{i}'
#         else:
#             str_mult +=f'*{i}'
#     return str_mult
n = int(input('Введите число: '))
multiplications = [math.factorial(i) for i in range(1, n+1)]
# multiplications_string = [mult(i) for i in range(1, n+1)]

print(f'List multiplications: {multiplications}')
# print(f'List multiplications: {multiplications_string}')