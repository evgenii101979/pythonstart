"""Чтение и запись файлов"""
"""создание файла с путями в папке С"""
# import os
# list_paths = []
# for adress, papka, file in os.walk('C:\\'):
#     for i in file:
#         full_path = os.path.join(adress, i)
#         list_paths.append(full_path)
# r = open('textdop7.txt', 'w', encoding='utf-8')
# for x in list_paths:
#     r.write(x + '\n')
# r.close()
""""""
# 'r' открыть для чтения (по умолчанию)
# 't' открыть в текстовом режиме (по умолчанию)
# 'w' открыть для записи, содкржимое файла удаляется, если файла нет создается новый
# 'a' открыть для дозаписи в конец файла, если файла нет создается новый
# 'b' открыть в бинарном режиме
# '+' открыть для чтения и записи 'r+', 'w+', 'a+'
""""""
# r = open('textdop7.txt', 'w', encoding='utf-8') # перекодирует в ютф-8
# r.write('строка текст')
# r.close()
""""""
# r = open('textdop7.txt', encoding='utf-8')
# u = r.read()
# print(u)        # строка текст
# r.close()
"""чтение в текстовом режиме"""
"""поиск в списке 'read.py'"""
# r = open('textdop7.txt', encoding='utf-8')
# for i in r:
#     if 'read.py' in i:
#         print(i)    # C:\Program Files\MySQL\MySQL Shell 8.0\lib\Python3.10\Lib\test\test_thread.py и т.д.
# r.close()
"""бинарный режим работы"""
"""создание копии файла .exe"""
# r = open('C:\Users\гендос\Desktop', 'rb')
# y = open('копия setup_0918.exe', 'wb')

# while True:
#     var = r.read(1048576)
#     print(var.__sizeof__())   # позволяет посмотреть сколько занимает объект места
#     # if var.__sizeof__() == 33:
#     #     break
#     y.write(var)

# print('контроль')
# r.close()
# y.close()

"""кодировка файлов"""

# r = open('text2.txt', 'w', encoding='utf-8')
# r.write('stroka текста')
# r.close()                       # stroka текста

# h = open('text2.txt')
# print(h.read())                     # stroka С‚РµРєСЃС‚Р° кирилица отображается не правильно

# h = open('text2.txt', encoding='utf-8')
# print(h.read())             # stroka текста прописываем кодировку и все норм

"""Строки, экранированные символы"""
"""множество"""
# t = {'a', 'f', 1, 1, 1, 1, 2, 3, 25, (2, 5)}
# y = set()
# print(t)            # {1, 2, 3, 'a', 25, (2, 5), 'f'} содержит уникальные эл. и выводит врасброс
""""""
# x = (1, 2, 3, 4, 5, 6, 7)       # кортеж
# y = [1, 2, 3, 4, 5, 6, 7]       # список
# u = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7}       # словарь
# h = {1, 2, 3, 4, 5, 6, 7}       # множество

# print(x.__sizeof__())        # (1, 2, 3, 4, 5, 6, 7)  80
# print(y.__sizeof__())        # [1, 2, 3, 4, 5, 6, 7]  104
# print(u.__sizeof__())        # {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7}   256
# print(h.__sizeof__())        # {1, 2, 3, 4, 5, 6, 7}  456
"""сравнение скорости работы списка и множества"""
# import time
# def f(*args):
#     list_new = []
#     for i in args:
#         for y in i:
#             if y not in list_new:
#                 list_new.append(y)
#     return list_new
    
# z = list(range(10000))
# x = list(range(5000, 15000))
# c = list(range(10000, 20000))
# start = time.time()
# f(z, x, c)
# stop = time.time() - start
# print(stop)                         # 2.4175496101379395 sec

# start2 = time.time()
# r = set(z)
# t = r.union(set(x), set(c))
# stop2 = time.time() - start2
# print(stop2)                        # 0.002000570297241211 sec
""""""
# z = {1, 2, 3, 4, 5}
# x = {3, 4, 5, 6, 7}
# # z.add(6)    # добавляет эл. в множество {1, 2, 3, 4, 5, 6}
# # z.discard(4)    # {1, 2, 3, 5, 6} удаляет эл
# # z.remove(4)     # тоже что и discard
# # y = z.union(x)    # объединяет множества{1, 2, 3, 4, 5, 6, 7}
# # z.update(x)         # так же объединяет множ.{1, 2, 3, 4, 5, 6, 7}
# # y = z.intersection(x)   # {3, 4, 5} находит общие эл. множ.
# y = z.difference(x)         # {1, 2} определяет разность множ. эл. 1 2 в множ z  нет в множ. х

# print(z)
# print(y)
"""применение множеств"""
# r = open('dop_lesson/textles7.txt', encoding='utf-8')
# # print(r.read().split()) # выводит список из всех слов без пробелов и знаков переноса строки: ['-', 'Очень', 'просто.', 'Хотя',
# print(set(r.read().split()))    # конвертруем список в множ. откидывает все повторяющиеся {'пришел,', 'Зашел', 'А', 'покрасился.',
""""""
# new = set()     # создаем новый словарь
# r = open('dop_lesson/textles7.txt', encoding='utf-8')
# new.update(set(r.read().split()))       # щбъединяем
# r.close()
# r = open('dop_lesson/textles71.txt', encoding='utf-8')
# new.update(set(r.read().split()))       # щбъединяем
# r.close()
# print(new)  # {'Хотя!..', 'варана.', 'воды', 'там', получаем уник. слова с обоих текстов
"""нахождение одинаковых слов в обоих текстах"""
# r = open('dop_lesson/textles7.txt', encoding='utf-8')
# r1 = set(r.read().split())
# r.close()
# r = open('dop_lesson/textles71.txt', encoding='utf-8')
# r2 = set(r.read().split())
# r.close()
# new = r1.intersection(r2)
# print(new)  # {'вот', 'его', 'в', 'а', 'с', 'время', 'на', 'и', 'это', 'тот', 'он',
            #'Но', 'не', 'немного', 'как', 'я', 'у', 'был', 'этот', 'что', 'по'}
""""""
# r = open('dop_lesson/textles7.txt', encoding='utf-8')
# r1 = set(r.read().split())
# r.close()
# r = open('dop_lesson/textles71.txt', encoding='utf-8')
# r2 = set(r.read().split())
# r.close()
# new = r1.difference(r2)
# print(new)  # {'ужина.', 'полтора', 'паре', \\ слова из r1 которых нет в r2





