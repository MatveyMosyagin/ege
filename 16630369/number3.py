from itertools import product
words = list(product(sorted('КОМПЬТЕР'), repeat=5))
res = []
a = 0
for x in words:
    a += 1
    if x.count('К') == 0 and x.count('Р') == 2 :
            res.append(a)
            print(a)

print(max(res))


