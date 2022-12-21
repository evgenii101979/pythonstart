"""Задача 1"""   #  В файле находится N натуральных чисел, записанных
# через пробел. Среди чисел не хватает одного, чтобы
# выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 4 6 7 -> 5
# data = [6, 4, 5, 3, 2, 8]
# data.sort()
# data = [data[i]-1 for i in range(1, len(data)) if data[i]-1 != data[i-1]]
# print(data)

# def task1():
#     with open('file_sem005.txt', 'r') as f:
#         lst = f.readline().split()
#     lst.sort()
#     lst = list(map(int, lst))
#     print(lst)
#     for i in range(1, len(lst)):
#         if lst[i] - 1 != lst[i - 1]:
#             print(lst[i] - 1)


"""Задача 2"""   #   Дан список чисел. Создайте список, в который попадают
# числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# 
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# def task2():
#     init_lst = [randint(1, 7) for i in range(20)]
#     init_lst = [1, 5, 2, 3, 4, 6, 1, 7]
#     print(init_lst)
#     lst = []
#     for j in range(len(init_lst)):
#         res_lst = []
#         res_lst.append(init_lst[j])
#         for i in range(j, len(init_lst)):
#             if init_lst[i] > res_lst[-1]:
#                 res_lst.append(init_lst[i])
#         # if len(res_lst) < 2:
#         #     res_lst = []
#         lst.append(res_lst)
#     lst2 = [lst3 for lst3 in lst if len(lst3) > 1]
#     print(lst2)


"""Задача 3"""  #   Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

# text = '''Она прожила в этом доме двадцать восемь лет, и только год из 
# всех этих долгих лет она не находилась под железной пятой 
# своей тетки Виолетты'''
# word = 'а'
# lst = text.split()
# new_lst = [s for s in lst if word not in s]
# print(text)
# new_text = ' '.join(new_lst)
# print(new_text)

# del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])
# print(del_st('абвгд гдежз жзе абв  ыопыпт', 'абв'))

def abc_delete(massage):
    find_txt = 'абв'
    lst = [i for i in massage.split() if find_txt not in i]
    return lst
    
# """"для игры крестики нолики"""

# def show_field():
#     global field
#     for i in range(0, len(field), 3):
#         print(field[i], field[i+1], field[i+2])
