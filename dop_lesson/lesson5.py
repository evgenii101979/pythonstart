"""Функции переменное количество аргументов, параметр *args"""

# def name(*args):       # астерикс
#     print(args)
# name(7, 9, 8, 7)    # (7, 9, 8, 7)

# def name(h, g, *args):
#     print(h)        # 1
#     print(g)        # 2
#     print(args)     # (3,)
# name(1, 2, 3)

# def name(h, g, *args, key): # key-ключевой параметр
#     print(h)        # 1
#     print(g)        # 2
#     print(args)     # (3, 4, 5, 6)
#     print(key)      # 10
# name(1, 2, 3, 4, 5, 6, key = 10)

"""функция приема и выдачи уникальных значений"""

# def exclusive_item(*args):
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
#     return new_list
# z = [9, 8, 7]
# x = [8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]
# t = exclusive_item(z, x, c)
# print(t)                        # [9, 8, 7, 6, 5, 1, 2, 3, 4]

# def exclusive_item(*args, key = False):
#     new_list = []
#     for i in args:
#         for y in i:
#             if y not in new_list:
#                 new_list.append(y)
#     if key == True:
#         new_list.sort()
#     return new_list
# z = [9, 8, 7]
# x = [8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]
# t = exclusive_item(z, x, c, key = True)
# print(t)                                    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""Функции, область видимости переменных"""

# x = 5
# count = 0
# while count < 3:
#     count += 1
# print(count)        # 3

# x = 5
# def name():
#     y = 10
#     print(x)
#     return y
# h = name()
# print(h)            # 5 10

# x = 5
# def name():
#     x = 10
#     print(x)        # 10  в функции значение изменилось
# name()
# print(x)        # 5 но глобальная переменная осталась

# x = 5
# def name():
#     global x        # меняет глобальную переменную
#     x = 100
#     print(x)        # 100  в функции значение изменилось
# name()
# print(x)            # 100

# x = 5
# def name():
#     x = 100
#     return x
# h = name()

# def name2():
#     print(h)            # 100
# name2()

"""можно записать структурированнее"""

# x = 5
# def name():
#     x = 100
#     return name2(x)

# def name2(par):
#     print(par)            # 100
# name()

"""ФУНКЦИЯ ОБЪЯВЛЕНА ФУНКЦИЕЙ"""

# x = 5
# def name():
#     x = 10
#     def name2():
#         x = 100
#         print(x)        # 100
#     name2()
#     print(x)            # 10
# name()
# print(x)                # 5

x = 5
def name():
    x = 10
    def name2():
        nonlocal x      # меняем переменную в материнской функции name()
        x = 100
        print(x)        # 100
    name2()
    print(x)            # 100
name()
print(x)                # 5
