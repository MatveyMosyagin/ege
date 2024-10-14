from itertools import product
words = list(product('МИТРОФАН', repeat=6))
a = f = 0
glas = 'ИОА'
soglas= 'МТРФН'
for x in words:
    glas1 = ''
    soglas1 = ''
    if len(set(x)) == len(x):
        f = 0
        for i in x:
            if i in glas:
                glas1 += i
            else:
                soglas1 += i
        if len(soglas1) > len(glas1):
            f = 0
            for i in range(5):
                if (x[i] in glas and x[i+1] in glas):
                    f = 1
            if f == 0:
                a += 1
print(a)