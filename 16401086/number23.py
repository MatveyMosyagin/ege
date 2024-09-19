a = open('23.txt').readline()
b = 1
res = 0
for i in range(0, len(a)-1):
    if a[i] not in 'ABC' or a[i+1] not in 'ABC':
        b += 1
    else:
        res = max(res, b)
        b = 1


print(res)