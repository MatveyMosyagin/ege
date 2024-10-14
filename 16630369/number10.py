from itertools import product
words = list(product('ГЕРАСИМ', repeat=7))
a = f = 0
glas = 'ЕАИ'
soglas= 'ГРСМ'
for x in words:
    if len(set(x)) == len(x):
        f = 0
        for i in range(6):
            if (x[i] in glas and x[i+1] in glas) or (x[i] in soglas and x[i+1] in soglas):
                f = 1
        if f == 0:
            a += 1
print(a)