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

4,43,14
