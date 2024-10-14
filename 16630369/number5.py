from itertools import product
words = list(product(sorted('АЛГОРИТМ'), repeat=4))
a = 0
for x in words:
    a += 1
    if x[0] == 'И' and x[1] == 'Г':
        print(a)
        break
