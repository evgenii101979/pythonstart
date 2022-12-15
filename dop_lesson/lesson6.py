"""Функции и структура кода"""
"""вычисление объема цилинра"""

# import math

# PI = math.pi

# def radius():
#     n = float(input('Диаметр цилиндра в см: '))
#     n /= 2
#     return n

# def height():
#     m = float(input('Высота цилиндра в см: '))
#     return m

# def volume():
#     r = radius()
#     h = height()
#     s = PI*r**2
#     v = s*h
#     return v
# print('Объем цилиндра', volume(), 'см3')

# def massa(g):
#     n = float(input('Удельный вес г/см3: '))
#     return g*n/1000
# print('Вес цилиндра в кг: ', massa(volume()))

"""Словари, тип данных dict"""

# d1 = {'a': 7}                     # пустой словарь
# d1['b'] = 9                         # добавляет ключ и новое значение
# d1['a'] = 8                         # заменяет в ключе на новое значение {'a': 8, 'b': 9}
# del d1['a']                         # удаляет значение по ключу {'b': 9}
# # print(d1)                           # {'a': 7}
# # print(d1['a'])                           # 7
# print(d1)                           # {'a': 7, 'b': 9}

# d1 = {'a': 7}
# d2 = dict(a=7)              # прописывает словарь
# d3 = dict.fromkeys([1, 2, 3, 4, 5], 'value')
# print(d1)                   # {'a': 7}
# print(d2)                   # {'a': 7}
# print(d3)                   # {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value'}

"""кассовый чек покупок"""

# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}  # 'meat'- ключ   : 3-значение закрепленное за ключом

# def buy():
#     pay = 0
#     while True:
#         enter = input('Что покупаем???\n')
#         if enter == 'end':
#             break
#         pay += price[enter]
#         print(pay)
#     print(pay)              # кассовый чек
#     return pay
# buy()        

"""вывод пароля"""
# users = {
#     'Alex7': {'password': 9856214, 'id': 1957},
#     'Jimmy99': {'password': 1236487, 'id': 9654},
#     'Bob33': {'password': 9546752, 'id': 6453}
#     }
# print(users['Alex7'] ['password'])          # 9856214

# d2 = dict([[1, 2], [3, 4], [5, 6]])
# print(d2)                           # {1: 2, 3: 4, 5: 6}


# d1 = {'a': 7, 'b': 9}       # словарь изменяемый тип данных
# d2 = dict([[1, 2], [3, 4], [5, 6]])              
# d3 = dict.fromkeys([1, 2, 3, 4, 5], 'value')

# d5 = d1.copy()                      # делает копию
# print(d1.items())                   # возвращает список из кортежей dict_items([('a', 7), ('b', 9)]) для работы со словарем при помощи цикла ФОР
# print(d1.keys())                   # возвращаянт ключи в словаре dict_keys(['a', 'b']) для ФОР
# print(d1.values())                    # возвоащает значения в словаре в виде списка dict_values([7, 9]) для ФОР
# d1.update(d2)
# print(d1)                           # {'a': 7, 'b': 9, 1: 2, 3: 4, 5: 6}

# if 'c' in d1:
#     d1['c']
# y = d1.get('c', 'value')        # проверяет есть ли такое значениеБ если нет то выдаст value
# print(y)

# t = d1.pop('a')
# print(t, d1)                    # 7 {'b': 9}

"""Словари, методы dict"""
"""переборка словарей методом ФОР"""

""""""
# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

# for i in price:
#     print(i)        # meat bread potato water выводит ключи словаря

# new_price = {}
# for i in price:
#     new_price[i] = round(price[i] * 0.85, 2)
# print(price)        # {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2} старый не изменен
# print(new_price)        # {'meat': 2.55, 'bread': 0.85, 'potato': 0.42, 'water': 0.17} новый со скидкой

""""""
# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

# new_price = {}
# x = price.items()
# for i in price:
#     new_price[i] = round(price[i] * 0.85, 2)
# print(x)            # dict_items([('meat', 3), ('bread', 1), ('potato', 0.5), ('water', 0.2)]) теперь в списке кортежи
# print(type(x))      # <class 'dict_items'>
# print(list(x))      # [('meat', 3), ('bread', 1), ('potato', 0.5), ('water', 0.2)] преобр. в список

""""""
# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
# for key, value in price.items():
#     #print(i)    # ('meat', 3) ('bread', 1) ('potato', 0.5) ('water', 0.2) выдает картежи
#     print(key)   # meat bread potato water  распаковали кортежи на ключи
#     print(value)    # 3 1 0.5 0.2 и значения

"""меняем местами ключи и значения"""
""""""
# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
# new = {}
# for key, value in price.items():
#     new[value] = key
# print(new)          # {3: 'meat', 1: 'bread', 0.5: 'potato', 0.2: 'water'}
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}
# new = {}
# x = price.values()
# for key, value in price.items():
#     new[value] = key
# # print(new)
# # print(x)        # dict_values([2, 1, 0.5, 0.2]) словарь в виде список из значений
# print(list(x))    # [2, 1, 0.5, 0.2] конверт. словарь в список

""""""
price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

for value in price.values():
    print(value)    # 2 1 0.5 0.2 
print(price.keys())     # dict_keys(['meat', 'bread', 'potato', 'water'])




