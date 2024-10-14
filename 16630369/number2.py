from itertools import product
words = list(product('АВЕИКНОР', repeat=3))
a = 0
for x in words:
    if x.count('В') == 1:
        a += 1
        if x.count('А') == 0:
            print(a)
            break