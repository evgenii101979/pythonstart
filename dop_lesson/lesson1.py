"""переменные"""
# a = b = 5
# print(a,b)      # 5 5

# n1, n2 = 5, 7
# print(n1, n2)   # 5 7

"""обмен"""

# sw1 = 8
# sw2 = 9
# # sw1, sw2 = sw2, sw1         # 9 8
# sw1, sw2 = sw2, sw1 + sw2   # 9 17
# print(sw1, sw2)
# sw2 -= a                    # 12
# print(sw2)

"""распаковка списка по переменым"""
            # * - arg

# z, x, c = [1, 2, 3]           # 1 2 3
# z, x, c = [1, 2, 3, 4, 5]     # ValueError: too many values to unpack (expected 3)
# z, x, *c = [1, 2, 3, 4, 5]      # 1 2 [3, 4, 5]
# z, *x, c = [1, 2, 3, 4, 5]      # 1 [2, 3, 4] 5
# *z, x, c = [1, 2, 3, 4, 5]          #  [1, 2, 3] 4 5
# print(z)                    # 1
# print(x)                    # 2
# print(c)                    # 3

"""типы данных"""

# a = None
# print(type(a))       # <class 'NoneType'>    -> отсутствие данных
# a = 1
# print(type(a))       # <class 'int'>         -> целое число
# a = 1.0
# print(type(a))       # <class 'float'>       -> число с плавающей точкой
# a = 1 + 1j
# print(type(a))       # <class 'complex'>     -> комплексное число
# a = '1'
# print(type(a))       # <class 'str'>         -> строка
# a = [1, 1, 'a']
# print(type(a))       # <class 'list'>        -> список
# a = (1, 1, 'a')
# print(type(a))       # <class 'tuple'>       -> кортеж
# a = {1, 1, 'a'}
# print(type(a))       # <class 'set'>         -> множество
# a = {'a':1, 'b':2}
# print(type(a))       # <class 'dict'>        -> словарь
# a = True
# print(type(a))       # <class 'bool'>        -> логические булевые значения

# a = 5 + 5               # 10
# b = 5.5 + 5             # 10.5
# c = 'str' + 'ing'       # string
# d = 5 + 'string'        # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a, b, c, d)          

"""конвертирующие функции"""

"""input"""

# x = input('Ввод')           
# print(type(x))              # Ввод 5 <class 'str'>
# r = x + 5
# print(r)                  # Ввод 5 TypeError: can only concatenate str (not "int") to str
# r = int(x) + 5
# print(r)                  # Ввод 5 10 
                            # Ввод 5.5 ValueError: invalid literal for int() with base 10: '5.5'
# r = float(x) + 5
# print(r)                    # Ввод 5.5 10.5
# r = float(5)
# print(r, type(r))           # 5.0 <class 'float'>
# r = int(5.9)
# print(r, type(r))           # 5 <class 'int'>

x = float(input('Введите число: '))
y = float(input('Введите число: '))
r = x + y
print(r)                                # Введите число: 5 Введите число: 6 11.0
print('результат: ' + str(r))           # Введите число: 6 Введите число: 8 результат: 14.0

30:00



