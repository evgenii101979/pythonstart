# 2'. Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [4, 2, -2, 3, -5, 8]
def pair_num(lst: list[int]) -> list[int]:
    res = []
    search = int(round((len(lst))+1)/2)
    for i in range(search):
        res.append(lst[i]*lst[-1-i])
    return res
print(pair_num(lst))
