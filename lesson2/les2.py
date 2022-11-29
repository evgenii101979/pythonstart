# 1     создание файла .txt и работа с ним

# colors=['red','green','blue']
# data=open('file.txt','a')           # а-создает, записывает и добавляет файл
#                                     # w-перезаписыввает файл заново
# #data.writelines(colors)             # разделителей не будет
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()

# 2     еще один способ создания и перезаписи

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# 3     читать данные из файла

# path='file.txt'           # для работы с числами произв. конверт. через int
# data=open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# 4      работа с функциями
#        вызов данных из соседнего файла

# import hello as h
# print(h.f(1))

# 5       ФУНКЦИЯ ВВОДА СТРОКИ И ЧИСЛА

# def new_string(simbol1, count=3):
#     return simbol1*count
# print(new_string('!', 5))           # !!!!!
# print(new_string('!'))              # !!!
# print(new_string(4))                # 12

# 6      ПЕРЕДАЧА НЕОГРАНИЧЕННОГО КОЛИЧЕСТВА АРГУМЕНТОВ

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))     # asdw
# print(concatenatio('a', '1', 'd', '2'))     # a1d2
# print(concatenatio('1', '2', '3', '4'))     # TypeError: ...

# 7       РЕКУРСИЯ (ФЕБОНАЧИ)

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list=[]
# for e in range(1,10):
#     list.append(fib(e))
# print(list)                 # 1 1 2 3 5 8 13 21 34

# 8       КОРТЕЖИ (НЕИЗМЕНЯЕМЫЙ СПИСОК)

# t=()
# print(type(t))                  # tuple
# t=(1,)
# print(type(t))                  # tuple
# t=(1)
# print(type(t))                  # int
# t=(28,9,1990)
# print(type(t))                  # tuple
# colors=['red','green','blue']
# print(colors)                  # ['red','green','blue']
# t=tuple(colors)
# print(t)                        # ('red','green','blue')

# a = (3, 4, 5)
# # print(a)
# # print(a[0])
# for item in a:
#     print(item)             # выводит все числа 3 4 5

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r: {} g: {} b: {}'.format(red, green, blue)) # r: red g: green b: blue

#  9       СЛОВАРИ(НЕУПОРЯДОЧЕННЫЕ КОЛЛЕКЦИИ ПРОИЗВОЛЬНЫХ
#            ОБЪЕКТОВ С ДОСТУПОМ ПО КЛЮЧУ)

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# # print(dictionary)     # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary['left'])   # ←
# # for k in dictionary.keys():
# #     print(k)                    # up left down right ключи выдает
# # for k in dictionary.values():
# #     print(k)                    # ↑ ← ↓ → выдает значения
# for v in dictionary:
#     print(v)                  # up left down right проходит по всему словарю
# for v in dictionary:
#     print(dictionary[v])        # ↑ ← ↓ → только значения

# 10     МНОЖЕСТВА

# ИЗМЕНЯЕМЫЕ

# colors = {'red', 'green', 'blue'}
# print(colors)           # {'blue', 'red', 'green'}
# colors.add('gray')
# print(colors)           # {'blue', 'red', 'green', 'gray'}
# colors.remove('red')
# print(colors)           # {'gray', 'green', 'blue'}
# colors.discard('red')
# print(colors)           # {'gray', 'blue', 'green'}
# colors.clear()
# print(colors)           # set()

# a = {1,2,3,5,8}
# b = {2,6,7,4,21}
# # c = a.copy()              # {1, 2, 3, 5, 8}
# # u = a.union(b)            # {1, 2, 3, 4, 5, 6, 7, 8, 21}
# # i = a.intersection(b)     # {2}
# # dl = a.difference(b)      # {8, 1, 3, 5}
# # dr = b.difference(a)      # {4, 21, 6, 7}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))  # {1, 3, 4, 5, 6, 7, 8, 21}
# print(q)

# НЕИЗМЕНЯЕМЫЕ

# s = frozenset(a)      # добавить и удалить ничего нельзя

# 11       СПИСКИ

# list1 = [1,2,3,4,5]
# list2 = list1
# list1[0] = 123          # меняя данные в списке 1 меняются и в списке 2
# list2[1] = 345          # меняя данные в списке 2 меняются и в списке 1
# print()
# for e in list1:
#     print(e)            # 1 2 3 4 5
# print()
# for e in list2:
#     print(e)            # 1 2 3 4 5

# list1 = [1,2,3,4,5]

# print(list1.append(11))      # добавляет цифру 11 последним элементом
# print(list1)

# print(list1.insert(2, 11))      # добавляет цифру 11 2-ым элементом
# print(list1)

# print(list1.pop(2))         # 3       удаляет 2 элемент 
# print(list1)                # [1, 2, 4, 5]

# print(list1)                # [1, 2, 3, 4, 5]
# print(list1.pop())          # 5
# print(list1)                # [1, 2, 3, 4]
# print(list1.pop())          # 4
# print(list1)                # [1, 2, 3]
# print(list1.pop())          # 3
# print(list1)                # [1, 2]
# print(list1.pop())          # 2
# print(list1)                # [1]
# print(list1.pop())          # 1





