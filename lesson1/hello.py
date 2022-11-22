#print('hello')
#value=None
##b=1.23
#print(type(a))
#print(type(b))
#value=2566
#print(type(value))
#s='hello world'
#print(a,'-', b,'-',s)
#print('{2} - {1} - {0}'.format(a,b,s)) # можно менять местами
#print(f'{a} - {b} - {s}')
#f=True
#print(f)

#list=['ddf', 'fef', 446, '+', 'dd', 1.555, True]
#print(list)

#print('Введите а');
#a=float(input())
#print('Введите b');
#b=float(input())
#print(a,'+', b,'=', a+b)
#print('{1} - {0}'.format(a,b)) # можно менять местами
#print(f'{a} - {b}')

# Арифметические операции

#a=3
#a+=5
#print(a)

# Логические операции

# f= [1,2,3,4]
# # print(f)
# # print(not 5 in f)
# is_odd=not f[0]%2
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a=int(input('введите число а'))     # поиск максимального числа
# b=int(input('введите число b'))
# if a>b:
#     print(a)
# else:
#     print(b)

# while

# original =23            #  перевернуть число
# inverted = 0
# while original != 0:
#     inverted = inverted *10+(original%10)
#     original//=10
#     print(original)
# else:
#     print('пожалуй')
#     print('хватит )')
# print(inverted)

# for

# for i in 1,2,3,4,5,6:       # вщзведение чисел в степень
#     print(i**3)

# list=[1,2,3,10,4,5]
# for i in list:       # вщзведение чисел в степень
#     # print(i)

# for i in range(2, 50, 6):       # выводит числа от 2 до 49 c прирощением 6
#     print(i)

# for i in 'gji kjio':       # выводит все буквы с пробелом и знаками
#     print(i)
# help(text.isalpha)              # встроенная функция помощи
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))                        # 39
# print('ещё'in text)                     # True
# print(text.isdigit())                   # False
# print(text.islower())                   # True
# print(text.replace('ещё', 'ЕЩЁ'))       # меняет прописные на заглавные

# for c in text:
#     print(c)                            # выводит текст побуквенно

# text = 'съешь ещё этих мягких французских булок' # с конца массива элементы считаются с -1
# print(text[0])                     # c
# print(text[1])                     # ъ
# #print(text[len(text)])             # IndexError
# print(text[len(text)-1])           # к
# print(text[-5])                    # б
# print(text[:])                     # print(text)
# print(text[:2])                     # съ
# print(text[len(text)-2:])          # ок
# print(text[2:9])                   # ешь ещё
# print(text[6:-18])                 # ещё этих мягких
# print(text[0:len(text):6])         # сеикакл
# print(text[::6])                   # сеикакл
# text=text[2:9]+text[-5]+text[:2]   # ...

# Списки   (базовые АПИ работы со списками)

# numbers=[1,2,3,4,5]
# print(numbers)                  # [1,2,3,4,5]
# ran=range(1,6)
# print(type(ran))
# numbers=list(ran)
# print(type(numbers))
# print(numbers)                  # [1,2,3,4,5]
# numbers[0]=10
# print(f'{len(numbers)} len')        # интерполяция
# print(numbers)                  # [10,2,3,4,5]
# for i in numbers:
#     i*=2
#     print(i)                    # [20,4,6,8,10]
# print(numbers)                  # [10,2,3,4,5]

# colors=['red','green','blue']
# for e in colors:
#     print(e)                        # red green blue
# for e in colors:
#     print(e*2)                      # redred greengreen blueblue
# colors.append('gray')               # добавить в конкец
# print(colors==['red','green','blue','gray'])        # True
# colors.remove('red')               # del colors[0]  # удалить элемент

# Функции

def f(x):
    if x ==1:
        return 'целое'
    elif x ==2.3:
        return 23
    else:
        return

arg =8
print(f(arg))
print(type(f(arg)))

# квадрат числа

# a=int(input())
# print(a**2)

# программа принимает 2 числа и проверяет является ли одно квадратом другого

# a=int(input('a '))
# b=int(input('b '))
# if a**2==b or b**2==a:
#     print('является')
# else:
#     print('Не является')

# принимает 5 чисел и ищет макс.

# a=input().split()
# print(a)
# max = int(a[0])
# for i in range(len(a)):
#     if int(a[i])>max:
#         max=int(a[i])
# print(max)

# a=list(map(float,input().split()))
# print(max(a))

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n=int(input('n '))
# a=[]
# b=''
# for i in range(-n,n+1):
#     a.append(i)
#     print(f' {i} ', end='')
#     b+=f' {i} '
# print()
# print(a)
# print(b)

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# n=abs(float(input('n ')))
# print(int(n * 10 % 10))

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a=float(input('a '))
if ((a % 5 == 0 and a % 10 == 0) or a % 15 == 0) and a % 30 != 0:
    print("Yes")
else:
    print("No")

