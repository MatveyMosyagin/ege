from itertools import product
words = list(product('МАТВЕЙ', repeat=6))
a = f = 0
for x in words:
    if len(set(x)) == len(x):
        f = 0
        for i in range(5):
            if x[0] == 'Й' or (x[i] == 'А' and x[i+1] == 'Е'):
                f = 1
        if f == 0:
            a += 1
print(a)