from itertools import product
words = list(product(sorted('МАНГУСТ'), repeat=6))
res = []
a = 0
for x in words:
    a += 1
    if x[0] != 'У' and x.count('М') == 2 and x.count('Г') < 2:
        res.append(a)
print(max(res))