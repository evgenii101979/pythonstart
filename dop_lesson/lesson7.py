"""Чтение и запись файлов"""
"""создание файла с путями в папке С"""
# import os
# list_paths = []
# for adress, papka, file in os.walk('C:\\'):
#     for i in file:
#         full_path = os.path.join(adress, i)
#         list_paths.append(full_path)
# r = open('textdop7.txt', 'w', encoding='utf-8')
# for x in list_paths:
#     r.write(x + '\n')
# r.close()
""""""
# 'r' открыть для чтения (по умолчанию)
# 't' открыть в текстовом режиме (по умолчанию)
# 'w' открыть для записи, содкржимое файла удаляется, если файла нет создается новый
# 'a' открыть для дозаписи в конец файла, если файла нет создается новый
# 'b' открыть в бинарном режиме
# '+' открыть для чтения и записи 'r+', 'w+', 'a+'
""""""
# r = open('textdop7.txt', 'w', encoding='utf-8') # перекодирует в ютф-8
# r.write('строка текст')
# r.close()
""""""
# r = open('textdop7.txt', encoding='utf-8')
# u = r.read()
# print(u)        # строка текст
# r.close()
"""чтение в текстовом режиме"""
"""поиск в списке 'read.py'"""
# r = open('textdop7.txt', encoding='utf-8')
# for i in r:
#     if 'read.py' in i:
#         print(i)    # C:\Program Files\MySQL\MySQL Shell 8.0\lib\Python3.10\Lib\test\test_thread.py и т.д.
# r.close()
"""бинарный режим работы"""
"""создание копии файла .exe"""
# r = open('C:\Users\гендос\Desktop', 'rb')
# y = open('копия setup_0918.exe', 'wb')

# while True:
#     var = r.read(1048576)
#     print(var.__sizeof__())   # позволяет посмотреть сколько занимает объект места
#     # if var.__sizeof__() == 33:
#     #     break
#     y.write(var)

# print('контроль')
# r.close()
# y.close()

"""кодировка файлов"""

# r = open('text2.txt', 'w', encoding='utf-8')
# r.write('stroka текста')
# r.close()                       # stroka текста

# h = open('text2.txt')
# print(h.read())                     # stroka С‚РµРєСЃС‚Р° кирилица отображается не правильно

h = open('text2.txt', encoding='utf-8')
print(h.read())             # stroka текста прописываем кодировку и все норм

4,05,30


