"""Игра в кости на python tkinter"""

# находится в папке кости

"""Декораторы"""
# оборачивает функцию в свой код модифицируя ее поведение не изменяя сам код функции

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def decor(f):
#     def wrapper():
#         print('код декоратора')
#         f()
#         print('второй код декоратора')
#     return wrapper

# @decor  # make = decor(make)

# def make():
#     enter = input('Enter something... ')
#     print(enter)
# print('здесь')
# make()

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# def decor(f):
#     def wrapper():
#         try:
#             h = f()
#         except Exception:
#             print('повторите ввод... ')     # повторите ввод... 
#             h = f()
#         return h
#     return wrapper

# @decor
# def make():
#     enter = float(input('введите число: '))
#     return enter
# @decor
# def make2():
#     enter = float(input('введите число опять: '))       
#     return enter

# make2() # введите число опять: khjk      введите число опять: 7
# make() # введите число: 8

"""Генераторы списков, словарей, множеств"""

# h = [9, 8, 7, 4, 5, 6, 2, 1, 5, 5]

# newh = []
# for x in h:
#     newh.append(x*2)
# print(newh)             # [18, 16, 14, 8, 10, 12, 4, 2, 10, 10]

# # тот же код только читаемее
# n = [x*2 for x in h]
# z = {x*2 for x in h}
# f = {x: x*2 for x in h}
# print(n)             # [18, 16, 14, 8, 10, 12, 4, 2, 10, 10]
# print(z)             # {2, 4, 8, 10, 12, 14, 16, 18}
# print(f)             # {9: 18, 8: 16, 7: 14, 4: 8, 5: 10, 6: 12, 2: 4, 1: 2}

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# h = [9, 8, 7, 4, 5, 6, 2, 1, 5, 5]
# newh = []
# for x in h:
#     if x % 2 == 0:
#         newh.append(x*2)
# print(newh)                    # [16, 8, 12, 4]
# g = [x for x in h if x % 2 == 0]
# print(g)                        # [8, 4, 6, 2]
# print(type(g))                        # <class 'list'>

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# h = [9, 8, 7, 4, 5, 6, 2, 1, 5, 5, -2]
# newh = []
# for x in h:
#     if x % 2 == 0:
#         newh.append(x*2)
# print(newh)                    # [16, 8, 12, 4, -4]
# g = [x for x in h if x % 2 == 0 and x > 0]
# print(g)                        # [8, 4, 6, 2]

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import os
# h = [9, 8, 7, 4, 5, 6, 2, 1, 5, 5, -2]
# g = [os.path.join(z, i) 
#     for z, x, c in os.walk('C:\\') 
#     for i in c if '.txt' in i]   # выдает список путей к заданным файлам
# # print(g)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}
new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)
print(new_price)            # {'meat': 1.7, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}
new_d = {i: round(price[i] * 0.85, 2) for i in price.keys()}
print(new_d)                # {'meat': 1.7, 'bread': 0.85, 'potato': 0.42, 'water': 0.17}




