# 2'. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
#  6 -> [2,3]
#  144 -> [2,3]

num = input('Введите натуральное число: ')
num = int(num.replace("-", ""))
lst = []
step = 2
while num > 1:
    if num % step == 0:
        lst.append(step)
        num = num/step
    else:
        step += 1
print(f"Список множителей {set(lst)}")