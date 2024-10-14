from itertools import product
words = list(product('РОСОМАХА', repeat=8))
a = 0
f = 0
glas = 'ОА'
soglas= 'РСМХ'
for x in words:
    if x.count('Р') == 1 and x.count('О') == 2 and x.count('С') == 1 and x.count('М') == 1 and x.count('А') == 2 and x.count('Х') == 1:
        f = 0
        for i in range(7):
            if (x[i] in glas and x[i+1] in glas) or (x[i] in soglas and x[i+1] in soglas):
                print(x)
                f = 1
            print(f)
        if f == 0:
            a += 1
print(a/16)