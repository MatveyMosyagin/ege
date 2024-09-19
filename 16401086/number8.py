from itertools import product
res = 0
a = list(product('АВЛОР', repeat=4))
for x in a:
    res += 1
    #print(x, res)
    if x[0] == 'Л':
        break
print(res)
