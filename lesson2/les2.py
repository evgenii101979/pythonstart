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

# path='file.txt'               # для работы с числами произв. конверт. через int
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

a=(3,4)
print(a)
print(a[0])

#  9       СЛОВАРИ(НЕУПОРЯДОЧЕННЫЕ КОЛЛЕКЦИИ ПРОИЗВОЛЬНЫХ
        # ОБЪЕКТОВ С ДОСТУПОМ ПО КЛЮЧУ)

# dictionary={}
# dictionary=\
#     {
#         'up': ''
#     }





