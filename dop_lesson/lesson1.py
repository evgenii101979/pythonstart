"""переменные"""
# a = b = 5
# print(a,b)      # 5 5

# n1, n2 = 5, 7
# print(n1, n2)   # 5 7

"""обмен"""

# sw1 = 8
# sw2 = 9
# # sw1, sw2 = sw2, sw1         # 9 8
# sw1, sw2 = sw2, sw1 + sw2   # 9 17
# print(sw1, sw2)
# sw2 -= a                    # 12
# print(sw2)

"""распаковка списка по переменым"""
            # * - arg

# z, x, c = [1, 2, 3]           # 1 2 3
# z, x, c = [1, 2, 3, 4, 5]     # ValueError: too many values to unpack (expected 3)
# z, x, *c = [1, 2, 3, 4, 5]      # 1 2 [3, 4, 5]
# z, *x, c = [1, 2, 3, 4, 5]      # 1 [2, 3, 4] 5
# *z, x, c = [1, 2, 3, 4, 5]          #  [1, 2, 3] 4 5
# print(z)                    # 1
# print(x)                    # 2
# print(c)                    # 3

"""типы данных"""

# a = None
# print(type(a))       # <class 'NoneType'>    -> отсутствие данных
# a = 1
# print(type(a))       # <class 'int'>         -> целое число
# a = 1.0
# print(type(a))       # <class 'float'>       -> число с плавающей точкой
# a = 1 + 1j
# print(type(a))       # <class 'complex'>     -> комплексное число
# a = '1'
# print(type(a))       # <class 'str'>         -> строка
# a = [1, 1, 'a']
# print(type(a))       # <class 'list'>        -> список
# a = (1, 1, 'a')
# print(type(a))       # <class 'tuple'>       -> кортеж
# a = {1, 1, 'a'}
# print(type(a))       # <class 'set'>         -> множество
# a = {'a':1, 'b':2}
# print(type(a))       # <class 'dict'>        -> словарь
# a = True
# print(type(a))       # <class 'bool'>        -> логические булевые значения

# a = 5 + 5               # 10
# b = 5.5 + 5             # 10.5
# c = 'str' + 'ing'       # string
# d = 5 + 'string'        # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a, b, c, d)          

"""конвертирующие функции"""

"""input"""

# x = input('Ввод')           
# print(type(x))              # Ввод 5 <class 'str'>
# r = x + 5
# print(r)                  # Ввод 5 TypeError: can only concatenate str (not "int") to str
# r = int(x) + 5
# print(r)                  # Ввод 5 10 
                            # Ввод 5.5 ValueError: invalid literal for int() with base 10: '5.5'
# r = float(x) + 5
# print(r)                    # Ввод 5.5 10.5
# r = float(5)
# print(r, type(r))           # 5.0 <class 'float'>
# r = int(5.9)
# print(r, type(r))           # 5 <class 'int'>

# x = float(input('Введите число: '))
# y = float(input('Введите число: '))
# r = x + y
# print(r)                                # Введите число: 5 Введите число: 6 11.0
# print('результат: ' + str(r))           # Введите число: 6 Введите число: 8 результат: 14.0

"""Условные операторы if, elif, else"""

# if True:                      # if
# if False:                       # elif
#     print('if')
# elif False:                     # else
#     print('elif')
# else:
#     print('else')

# a = 4 == 4
# print(a)                         # True
# a = 4 == 5
# print(a)                         # False
# a = 4 <= 3
# print(a)                         # False

# x = -5
# if x == 0:                      # if
# # if x > 0                        # elif
#     print('if')
# #elif False:                     # else
# elif x > 0:                   #  x = 3 # elif
#     print('elif')
# else:                         #  x = -5 'else'
#     print('else')

# x = 0                  # x=5  сразу будет ответ
# if x == 0:              # x = 0 делает условие и потом ответ 5,0
#     x += 1
# print(5/x)

# x = -5.22                                        # x = 0 x был равен 0 100.0
# if  x == 0:    # not                             # x = 5 x допустимое значение 20.0
#     x = 1                                        # x = [1, 2, 3] В x недопустимый тип данных 100.0
#     print('x был равен 0')                       # x = -5.22 x допустимое значение -19.157088122605366
# elif type(x) == type(5) or type(x) == type(5.5):        # and
#     print('x допустимое значение')
# else:
#     print('В x недопустимый тип данных')
#     x = 1
# print(100/x)

# import os
# sayt = input()                          # youtube.com else
# if 'https://' in sayt:                  # www.youtube.com elif
#     os.system('start ' + sayt)          # https://www.youtube.com/ if
#     print('if')
# elif 'www.' in sayt:
#     sayt = 'https://' + sayt
#     os.system('start ' + sayt)
#     print('elif')
# else:
#     sayt = 'https://www.' + sayt
#     os.system('start ' + sayt)
#     print('else')

# import os
# import time
# os.system('start ' + 'https://www.youtube.com')         # откроет ютуб
# time.sleep(5)                                           # через 5 сек
# os.startfile('D:\игры\край мира\KrayMira\master.exe')   # откроет игру