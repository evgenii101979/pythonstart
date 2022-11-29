# 2'. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

xpred = [True, False]
ypred = [True, False]
zpred = [True, False]
for i in range(2):
    xpred[i]
for x in xpred:
    for y in ypred:
        for z in zpred:
            print(x, y, z)
            res1 = not (x or y or z)
            res2 = (not x) and (not y) and (not z)
            print(res1 == res2)

