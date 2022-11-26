# создание файла .txt и работа с ним

# colors=['red','green','blue']
# data=open('file.txt','a')           # а-создает, записывает и добавляет файл
#                                     # w-перезаписыввает файл заново
# #data.writelines(colors)             # разделителей не будет
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()

# еще один способ создания и перезаписи

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# читать данные из файла

# path='file.txt'               # для работы с числами произвести конвертацию через int
# data=open(path, 'r')
# for line in data:
#     print(line)
# data.close()

#  работа с функциями

# def f(x):
#     if x ==1:
#         return 'целое'
#     elif x ==2.3:
#         return 23
#     else:
#         return

# arg =8
# print(f(arg))
# print(type(f(arg)))

import hello

print(hello.f)
