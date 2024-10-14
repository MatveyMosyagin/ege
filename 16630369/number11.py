from itertools import *
a = 0
f = 0
glas = 'ОА'
soglas= 'РСМХ'
for x in permutations('РОСОМАХА'):
        f = 0
        for i in range(7):
            if (x[i] in glas and x[i+1] in glas) or (x[i] in soglas and x[i+1] in soglas):
                f = 1
        if f == 0:
            print(x)
            a += 1
print(a/4)