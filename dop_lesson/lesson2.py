"""Цикл while"""

# x = 0               # считает сколько проходов
# while x < 5:        # для цикла обязателен счетчик x = 0
#     x += 1          # каждый раз прибавдяет проход
#     print(x)        # 1 2 3 4 5
# else:
#     print(x)        # 5

"""факториал числа (5 = 1*2*3*4*5 = 120)"""

# x = int(input())
# count = 0
# y = 1
# while count < x:
#     count += 1
#     y *= count
#     print(y)            # 1 2 6 24 120
# else:
#     print(y)            # 120

# поместим эту программу в цикл

# while True:                 # дает возможность после отработки числа ввести еще число и т.д.
#     x = int(input())        # инпут в данном случае является остановкой цикла
#     count = 0
#     y = 1
#     while count < x:
#         count += 1
#         y *= count
#     else:
#         print(y)        # 5 -> 120// 6 -> 720// 7 -> 5040

# x = ''                              # ввод данных h
# while len(x) < 5:                   # ввод данных e
#     y = input('ввод данных ')       # ввод данных l
#     x += y                          # ввод данных l         # ввод данных h
# else:                               # ввод данных o         # ввод данных ello
#     print(x)                        # hello

# x = ''                              
# while len(x) < 5:                   
#     y = input('ввод данных ')
#     if y == 'o':
#         continue            #  на букве о перезапускает цикл   ввод данных h e l  l o o y    helly
#     if y == 'l':
#         break               # полностью прекращает работу цикла и else не исполняется
#     x += y                  # ввод данных р р е l окончание программы
# else:
#     print(x)        
# print('программа работает дальше') # ввод данных р l  /// программа работает дальше

# import os

# while True:                                 # каждый раз цикл будет возвращать к вводу данных
#     sayt = input('Введите адрес сайта\n')  # youtube.com else
#     if sayt == 'завершить':                 # при вводе завершить заканчивает программу
#         break
#     if 'https://' in sayt:                  # www.youtube.com elif
#         os.system('start ' + sayt)          # https://www.youtube.com/ if
#         print('if')
#     elif 'www.' in sayt:
#         sayt = 'https://' + sayt
#         os.system('start ' + sayt)
#         print('elif')
#     else:
#         sayt = 'https://www.' + sayt
#         os.system('start ' + sayt)
#         print('else')

"""Цикл for"""          # позволяет перебрать элемнты последовательности

# for i in 'stroka text': # stroka text
# m = 'stroka text'
# count = 0
# for i in m:
#     if i == 't':
#         continue
#         print('В строке есть буква t')
#         count += 1
#     print(i)    # srokaex /// цикл завершен, букв t 0 /// программа работает дальше
#     # if i == 'a':
#     #     break       # В строке есть буква t /// программа работает дальше
# else:
#     print('цикл завершен, букв t', count)   # цикл завершен, букв t 3
#     # print(i)
# print('программа работает дальше')

"""Цикл for, цикл в цикле"""

# x = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# y = input('введите строку:\n')
# for i in x:
#     count = 0
#     for r in y:
#         if i == r:
#             count += 1
#     if count > 0:      # строка текста ?? букв а было 2 ?? е было 1 ?? 
#         print('букв', i, 'было', count)# к было 2 ?? о было 1 ?? р было 1 ?? с было 2 ?? т было 3

# for x in range(10):   # (start, stop, step) # 0 1 2 3 4 5 6 7 8 9
# for x in range(5, 10):  # 5 6 7 8 9
# for x in range(1, 10, 2): # 1 3 5 7 9
# for x in range(10, -10, -2):# 10 8 6 4 2 0 -2 -4 -6 -8
#     print(x)

01:29:36 python hub studio



