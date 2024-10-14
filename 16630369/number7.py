from itertools import product
words = list(product('012345678', repeat=5))
a = 0
for x in words:
    if int(x[0]) > int(x[1]) > int(x[2]) > int(x[3]) > int(x[4]):
       a += 1

print(a)