"""Выражение генератор"""

# h = ['http\\www.сайт.com', 'http\\www.какойтосайт.net', 
#     'http\\www.левыйсайт.com', 'http\\www.другойсайт.com', 
#     'http\\www.сайтишка.net', 'http\\www.сайтец.com']

# n = [x.split('\\')[1] for x in h if '.com' in x]      # генератор списка    <class 'list'>
# print(type(n))        # ['www.сайт.com', 'www.левыйсайт.com', 'www.другойсайт.com', 'www.сайтец.com']
# z = (x.split('\\')[1] for x in h if '.com' in x)      # выражение генератор   <class 'generator'>
# for i in z:        # www.сайт.com www.левыйсайт.com www.другойсайт.com www.сайтец.com
#     print(i)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# n = [x.split('\\')[1] for x in h if '.com' in x]
# z = (x.split('\\')[1] for x in h if '.com' in x)
# print(next(z))          # www.сайт.com
# print(next(z))          # www.левыйсайт.com
# print(next(z))          # www.другойсайт.com
# print(next(z))          # www.сайтец.com
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import os
# n = [x for x in os.walk('C:\\')]        # очень много времени выжает все
# print('здесь')
# z = [y for y in os.walk('C:\\')]        # выдает быстро по одному значению по порядку
# print('тут')
# n.__sizeof__()
# print(z.__sizeof__())       # 1283144
# next(z)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""Функция генератор, оператор yield"""
# def some():
#     list_text = []
#     with open('D:/учеба 2/python/HelloPython/dop_lesson/textgen.txt', encoding='utf-8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text                # ['строка', 'текста']
#                                     # ['с', 'какой-то']
#                                     # ['информацией']
# for i in some():
#     print(i.split())
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def some():
#     with open('D:/учеба 2/python/HelloPython/dop_lesson/textgen.txt', encoding='utf-8') as r:
#             for x in r:
#                 yield x
# for i in some():
#     print(i.split())
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def some():
#     with open('D:/учеба 2/python/HelloPython/dop_lesson/textgen.txt', encoding='utf-8') as r:
#             for x in r:
#                 yield x
# p = some()
# print(next(p))      # строка текста
# print(next(p))      # с какой-то с какой-то
# print(next(p))      # информацией  
# for i in p:
#     print(i)        # строка текста
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""lambda функция"""
# анонимные функции
# def some(x):
#     return x/5
# var = lambda x: x / 5                # тоже что и def some() return  стоит по уимолчанию и писать не надо
# print(some(7))          # 1.4
# print(var(7))           # 1.4
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""sorted"""
# list_of = [['adam', 29], ['jonny', 3*1/12], ['jess', 25]]
# def s(x):
#     return x[1]
# r = sorted(list_of, key=lambda x: x[1])  # функция сортирует списки по ключу
# print(r)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""filter"""
list_of = [['adam', 29], ['jonny', 3*1/12], ['jess', 25]]
x = list(filter(lambda x: x[1] > 18, list_of)) # фильтрует по признаку
print(x)








