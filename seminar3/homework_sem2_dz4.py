# 4'. Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

with open('file.txt', 'r') as f:
    lst = f.read().split('\n')
lst = list(map(int, lst))
num = int(input('Введите число: '))
mass = [i for i in range(-num, num+1)]
step = 1
for pos in lst:
    step *= mass[pos]
print(lst)
print(mass)
print(step)