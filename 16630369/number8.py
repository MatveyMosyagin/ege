from itertools import product
words = list(product('ABCDXYZ', repeat=4))
a = 0
for x in words:
    if x[0] in 'XYZ' and x[1] not in 'XYZ' and x[2] not in 'XYZ' and x[3] not in 'XYZ':
        a += 1

print(a)