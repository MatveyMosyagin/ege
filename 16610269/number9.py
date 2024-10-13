from itertools import product

a = 0
words = list(product('12345678', repeat=5))
for x in words:
    if x[0] < x[1] < x[2] < x[3] < x[4]:
        a += 1
print(a)
