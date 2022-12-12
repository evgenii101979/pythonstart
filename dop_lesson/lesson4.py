"""Практика python, модуль os, функция walk"""

('D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк',
['волк', 'маша'], ['веня.txt', 'жора.txt', 'клуб.jpg'])

# import os
# import time

# for i in os.walk('D:\\учеба 2\дополнительно\файлы питон дополнительно\пример волк'):  # позволяет сгенерировать пути наподобие поиска на виндовс с фильтрами
#     print(i)    # ['волк', 'маша'], ['веня.txt', 'жора.txt', 'клуб.jpg']
#                 # волк', [], ['10.jpg', 'Безымянный.png']
#                 # маша', [], ['IMG_20181127_151708.jpg', 'доверенность на газификацию.docx']

# spisok = []
# for adress, dirs, files in os.walk('D:\\учеба 2\дополнительно\файлы питон дополнительно\пример волк'):
#     # spisok.append(adress) # в список добавляет все пути к папкам по данному адресу
#     for file in files:
#         spisok.append(os.path.join(adress, file)) # ['D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\веня.txt',
#                                                     #'D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\жора.txt',
# # выводит пути ко всем файлам по заданному адресу   # 'D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\клуб.jpg',
#                                                     # 'D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\волк\\10.jpg',
#                                                     # 'D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\волк\\Безымянный.png',
#                                                     # 'D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\маша\\IMG_20181127_151708.jpg',
#                                                     # 'D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\маша\\доверенность на газификацию.docx']
# print(spisok)

# spisok = []
# for adress, dirs, files in os.walk('D:\\учеба 2\дополнительно\файлы питон дополнительно\пример волк'):
#     for file in files:
#         full = os.path.join(adress, file)
#         if '.txt' in full:                  # ['D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\веня.txt',
#                                             # 'D:\\учеба 2\\дополнительно\\файлы питон дополнительно\\пример волк\\жора.txt']
#             spisok.append(full)             # выбирает только файлы .txt и пути к ним
# print(spisok)

"""добавление в список файлов по адресу созданных в течении суток по заданному адресу"""

# spisok = []
# for adress, dirs, files in os.walk('D:\\учеба 2\дополнительно\файлы питон дополнительно\пример волк'):
#     for file in files:
#         full = os.path.join(adress, file)
#         if time.time() - os.path.getctime(full) < 86400: 
#             spisok.append(full)
# print(spisok)

"""Функции def, определение и вызов"""  # скрытый участок кода, выпоняемый по нашей команде

# print('до функции')                 # до функции
# def show():
#     print('функция')
# show()                              # функция
# print('после функции')              # после функции
# show()                              # функция

# def show():
#     print('функция')
# def show2():
#     x = 7
#     return x                          # возвращает результат работы функции в точку запуска
# y = show2()                       # запуск функции через переменную с возвратом значения
# z = show2() + 9
# print(y)                              # 7
# print(z)                              # 16
# show()                        # функция
# print(show())                   # None
# print(x)                        # NameError: name 'x' is not defined, переменную из функции принт не видит

# def show():
#     print('функция')
# def show2():
#     x = 7 + z
#     return x
# z = 7
# y = show2()
# print(y)                    # 14
# z = 9
# t = show2()
# print(show2())              # 16

"""Функции def, параметры и аргументы"""

# def count_list(par): # параметр  # функция определения длины списка
#     count = 0
#     for i in par:
#         count += 1
#     return count
# j = [9, 8, 7, 6]
# print(count_list(j))  # аргумент       # 4
# h = ['a', 'a', 'h']
# print(count_list(h))        # 3
# k = [9, 8, 7, 5, 7, 5]
# print(count_list(k))        # 6
# print(count_list('strokajjj'))        # 9

"""считает длину списка"""

# def count_list(par, count): # параметр  # функция определения длины списка. можно убрать =0 у count = 0
#     for i in par:
#         count += 1
#     return count
# j = [9, 8, 7, 6]
# print(count_list(j, 0))  # аргумент       # 4    и поставить 0 в принт 2 аргументом

"""определение индекса последнего элемента"""

# def count_list(par, count = 0): # параметр  # функция определения индекс последнего элемента
#     for i in par:
#         count += 1
#     return count
# j = [9, 8, 7, 6, 8, 9, 7, 0, 4]
# print(count_list(j, -1))  # аргумент       # 8

# def count_list(par, par2 = False, count = 0): # параметр  # функция определения длины списка
#     if par2 == True:
#         typ = type(par[0])
#         for i in par:
#             count += 1
#         return count, typ
#     else:
#         for i in par:
#             count += 1
#         return count
# j = [9, 8, 7, 6, 8, 9, 7, 0, 4]
# print(count_list(j))  # аргумент

def count_list(par, par2 = False, count = 0): # параметр  # функция определения длины списка
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count
j = [9, 8, 7, 6, 8, 9, 7, 0, 4]
print(count_list(j, count=-1))  # аргумент  # 8
print(count_list(j, True))  # (9, <class 'int'>)
print(count_list(j, True, -1))  # (8, <class 'int'>) кортеж
h, p = count_list(j, True)      # распаковка кортежа
print(h, p)                     # 9 <class 'int'>

