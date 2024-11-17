from itertools import product

a = 0
words = list(product('0123', repeat=3))
for x in words:
    if int(x[0]) != 0 and int(x[0])+int(x[2]) > int(x[1]):
        a += 1
print(a)