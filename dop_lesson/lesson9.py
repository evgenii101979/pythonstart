"""Менеджер контекста with as"""

# try:
#     r = open('textles9.txt', 'a')
#     r.write('something' + '\n')
#     10/0
#     r.write('что-то')   #, encoding='utf-8'
# finally:
#     r.close()   # закроет всегда если будет ошибка, и запись до ошибки сохранится

# print('все норм')

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# из функ. опен открыть как р
# with open('textles9.txt', 'a') as r: # виз открывает и закрывает файл в любом случае
#     r.write('something' + '\n')
#     10/0                             # на ошибке файл закроется но первая запись останется
#     r.write('что-то')   #, encoding='utf-8'
# print('все норм')












