"""анонимные, lambda функции"""

# def f(x):
#     x**2
# g = f
# # print(type(f))          # <class 'function'>
# print(f(1))          # None
# print(g(1))          # None

# def f(x):
#     return x ** 2
# g = f
# print(f(2))             # 4
# print(f(4))             # 16
# print(g(4))             # 16

# def calc(x):
#     return x+10
    
# print(calc(10))             # 20

# def calc2(x):
#     return x*10
# print(calc2(10))             # 100

# def math(op, x):
#     print(op(x))
# math(calc2, 10)             # 100
# math(calc, 10)             # 100

"""lambda"""

# sum = lambda x, y: x+y        # def sum(x, y):
#                               #     return x+y

# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# calc(mult, 4, 5)                    # 20
# calc(sum, 4, 5)                    # 9
# calc(lambda x, y: x+y , 4, 5)   # 9

"""List Comprehension"""    # быстро создавать списки

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# def f(x):
#     return x**3

# list = [i for i in range(1, 21)] # список от 1 до 20 -> # list = []
#                                                         # for i in range(1, 21):
#                                                         #     list.append(i)
# list1 = [i for i in range(1, 21) if i % 2 == 0]         #     if(i % 2 == 0):
# list2 = [(i, i) for i in range(1, 21) if i % 2 == 0]    # с кортежами
# list3 = [f(i) for i in range(1, 21) if i % 2 == 0]      # кубы четных чисел от 1 до 20     
# list4 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]    # число и его куб четных чисел от 1 до 20                                                
                                                    
# print(list)
# print(list1)
# print(list2)
# print(list3)
# print(list4)

"""выбрать четные числа из файла и составить список пар (число; квадр.числа)"""
# 1 2 3 5 8 15 23 38
# [(2, 4), (8, 64), (38, 1444)]

# path = 'lesson3/file_lam.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

                                            # def select(f, col):
                                            #     return [f(x) for x in col]
                                            # def where(f, col):
                                            #    return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

""""map"""

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)
# data1 = list(map(int, '1 2 3 4 55 55 65'.split()))
# for e in data1:
#     print(e)
# print('--')
# for e in data1:
#     print(e)

"""filter"""

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

"""zip"""

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [11, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)                     # [('user1', 4, 11), ('user2', 5, 222), ('user3', 9, 333)]

"""функция enumerate"""

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [11, 222, 333]
# data = list(enumerate(users))
# print(data)                     # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]


