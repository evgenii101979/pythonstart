# 5'. Реализуйте алгоритм перемешивания списка.

from random import randint
list1 = [1, 2, 3, 4, 5]
for i in range(len(list1)-1):
    n = randint(0, len(list1)-1)
    list1[i], list1[n] = list1[n], list1[i]
print(list1)
