"""Строки, экранированные символы"""
# s = "Lets write a string as 's'"
# print(s)    # Lets write a string as 's'

# s = 'Let\'s write a string as "s"'
# print(s)    # Let's write a string as "s"

# s = 'Lets \
# write a \
# string as s'
# print(s)    # Lets write a string as s

# s = 'Lets write a stri\ng as s' # Lets write a stri
#                                 # g as s
# print(s)

# url = 'https:\www.yutube.com'
# print(url)      # https:\www.yutube.com

# url = 'https:\www.yutube.com\new'       # https:\www.yutube.com
#                                         # ew
# print(url)

# url = 'https:\www.yutube.com\\new'       # https:\www.yutube.com\new
# print(url)

# url = r'https:\\www.yutube.com\new'       # https:\www.yutube.com\new
# url = 'https:\\www.yutube.com\\new'         # https:\www.yutube.com\new
# print(url)

# x = 'C:\\Users\\PyHS\\Desktop'
# print(x)            # C:\Users\PyHS\Desktop

# x = 'C:/Users/PyHS/Desktop'
# print(x)                # C:/Users/PyHS/Desktop

"""Строки, методы str"""

# s = 'sTROka teksta'
# print(s[0:5])   # strok
# print(s[5])         # a
# print('stro' in s)     # True
# print(s.upper())        # STROKA TEKSTA переводит всю строку в заглавные
# print(s.lower())        # stroka teksta в нижний регистр
# print(s.capitalize())       # Stroka teksta первая буква станет заглавной

# path = 'C:/Users/PyHS/Desktop/s.py'
# path1 = path.replace('/', '\\')
# print(path1)        # C:\Users\PyHS\Desktop\s.py меняет символы на другие

# r = path1.split('\\')
# print(r)            # ['C:', 'Users', 'PyHS', 'Desktop', 's.py'] разбивает список по указанному разделителю
# print(r[-1])        # s.py   получаем последний эл. списка т.е. имя файла

"""редактирование текста"""

# q = open('D:\учеба 2\python\dop les8.txt', encoding='utf-8')
# print(q.read())           # читает текст из заданного файла

# q = open('D:\учеба 2\python\dop les8.txt', encoding='utf-8')
# r1 = q.read()
# list_znk = ['(', ')', ',', '"', '\n']
# for i in list_znk:
#     r1 = r1.replace(i, '')
# print(r1)           # удаление заданных знаки
# r2 = r1.split()
# print(r2)       # разбили по разделителю и получили список ['Далекое', 'будущее', 'космические', .....

# new_text = ' $ '.join(r2)
# print(new_text)   # Далекое $ будущее $ космические $ корабли $..... собрали текст заново с заданным разделителем

"""f-строка, форматирование строк"""

# enter = input('Your name: ')
# s = 'Hello %s, I am %s' % (enter, 'Python')          # %s подставить строку в неизменном виде
# print(s)                                            # Your name: gena   # Hello gena # Hello gena, I am Python

# s1 = 'Hello {}, I am {}'.format(enter, 'Python')        # Hello gena, I am Python
# s1 = 'Hello {1}, I am {0}'.format(enter, 'Python')      # Hello Python, I am gena
# print(s1)

# s2 = f'Hello {enter}, I can do it in f-string {2**3}'    # Hello gena, I can do it in f-string 8
# print(s2)

# var = 'Stroka'
# s3 = f'Hello {enter}, I can do it in f-string {len(var)}'    # Hello gena, I can do it in f-string 6
# print(s3)

"""Обработка исключений, try, except"""

# while True:     # бесконечный цикл пока не выпонится условие
#     try:                                        # в блок трай вносим код где возможна ошибка
#         enter = float(input('Введите число '))
#         break           # если условие выполнится то цикл вайл закончится брейком
#     except ValueError:                 # если не прописать ошибку то будет при любой ошибке выполнять следующий код
#         print('не корректный ввод')
# print('все норм')

# while True:     # бесконечный цикл пока не выпонится условие
#     try:                                        # в блок трай вносим код где возможна ошибка
#         enter = float(input('Введите число '))
#         print(100/enter)
#         break           # если условие выполнится то цикл вайл закончится брейком
#     except ValueError:                 # если не прописать ошибку то будет при любой ошибке выполнять следующий код
#         print('не корректный ввод')
#     except ZeroDivisionError:       # так же прописываем другие возможные ошибки
#         print('делить на 0 нельзя')
#     else:                   # необязательный оператор, прописывается только если нет ошибки в блоке трай
#         print('Пользователь молодец') # брейк не даст выпонить эту команду, но убрав его выпоняется
#     finally:        # блок исполняется всегда для сохранения данных при ошибке
#         print('Вывод финали')
# print('все норм')

import sys

url_list = ['D:\учеба 2\python\HelloPython\dop_lesson\doples81.txt',\
    'D:\учеба 2\python\HelloPython\dop_lesson\doples82.txt',\
    'text25.txt',\
    'D:\учеба 2\python\HelloPython\dop_lesson\doples83.txt']

list_defect = []
list_info = []
try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())  # прочитает файлы
        except Exception:           # все ошибки такого плана
            list_defect.append(url)     # добавит в список дефф.файлов
            sys.exit()  # закрывает программу если ошибка не может быть обработана
            continue
finally:
    r = open('save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print('я все сука помню')
