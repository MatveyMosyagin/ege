from itertools import product
words = list(product('АБЗИ', repeat=4))
a = 0
for x in words:
    a += 1
    if x == ('И', 'З', 'Б', 'А'):
        print(a)
        break
