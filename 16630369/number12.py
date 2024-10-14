from itertools import product
words = list(product('01234567', repeat=5))
a = 0
nechet = '1357'
for x in words:
    f = 0
    if x[0] != '0' and x.count('6') == 1:
        for i in range(4):
            if (x[i] in nechet and x[i + 1] == "6") or (x[i+1] in nechet and x[i] == "6"):
                f = 1
        if f == 0:
            a += 1

print(a)