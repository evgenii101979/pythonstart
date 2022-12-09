# import random
# candys = 117

# def input_candy():
#     global candys
#     while True:
#         move = int(input('Введите конфеты '))
#         if move > 0 and move < 29 and move <= candys:
#             candys -= move
#             break
#         else:
#             print('Столько взять нельзя')

# def bot_take():
#     global candys
#     move = random.randint(1, 28)
#     print(f'Бот взял {move}')
#     candys -= move

# print(f'На столе лежит {candys} конфет')
# players = ['Пользователь', "Компьютер"]
# move = random.choice(players)
# print(f'Первым ходит - {move}')
# while True:
#     if move == 'Пользователь':
#         input_candy()
#         print(f'Осталось {candys}')
#         move = "Компьютер"
#     else:
#         bot_take()
#         print(f'Осталось {candys}')
#         move = 'Пользователь'
#     if candys < 29:
#         print(f'Победил {move}')
#         break

# from random import randint
# def is_victory(field):
#     vin = False
#     combs = [[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [0, 3, 6],
#              [1, 4, 7],
#              [2, 5, 8],
#              [0, 4, 8],
#              [2, 4, 6]]
#     for pos in combs:
#         if field[pos[0]] == field[pos[1]] == field[pos[2]]:
#             vin = True
#             break
#     return vin


# def spare(field):
#     count = 0
#     for i in field:
#         if type(i) == str:

# while True:
#     if move == 'Пользователь':
#         print('-'*10)
#         input_pos()
#         show_field()
#         print('-'*10)
#         move = "Компьютер"
#         if is_victory(field):
#             print('Пользователь победил')
#             break
#     else:
#         bot_move()
#         print('Бот сделал ход')
#         show_field()
#         print('-'*10)
#         move = 'Пользователь'
#         if is_victory(field):
#             print('Робот победил')
#             break
#     if spare(field):
#         print('Ничья')
#         break



"""Задача 1""" # Вводятся названия городов в одну строчку через пробел.
# Необходимо определить функцию map, которая бы возвращала названия
# городов только длиной более 5 символов. Вместо остальных названий -
# строку с дефисом ("-").
# Сформировать список из полученных значений и отобразить
# его на экране в одну строчку через пробел.

# Ввод:
# Москва Уфа Вологда Тула Владивосток Хабаровск
# Вывод:
# Москва, -, Вологда, -, Владивосток, Хабаровск

# lst = 'Москва,Уфа,Вологда,Тула,Владивосток,Хабаровск'.split(',')
# for i in range(len(lst)):
#     if len(lst[i]) <= 5:
#         lst[i] = "-"
# print(','.join(lst))

# citys = 'Москва,Уфа,Вологда,Тула,Владивосток,Хабаровск'
# a = list(map((lambda x: x if len(x) > 5 else '-'), citys.split(',')))
# print(','.join(a))

"""Задача 2."""

# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))

# Ввод:
# house=дом car=машина men=человек tree=дерево
# Вывод:
# (('house', 'дом'), ('car', 'машина'), ('men', 'человек'), ('tree', 'дерево'))

# c = 'house=дом car=машина men=человек tree=дерево'
# ListC = c.split(' ')
# # ListC = list(c.items(' '.join(i for i in c.split(' '))))
# a = {'house': 'дом', 'car': 'машина', 'men': 'человек', 'tree': 'дерево'}
# b = list(a.items())
# print(b)
# print(ListC)
# d = tuple(map(lambda x: tuple(x.split('=')), ListC))
# # ListD = list(d.items(' '.join(i for i in d.split(' '))))
# print(d)

a = 'house=дом car=машина men=человек tree=дерево'.split()
a = tuple(map(lambda x: tuple(x.split('=')),a))
print(a)
