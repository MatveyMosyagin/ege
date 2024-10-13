a = [int(i) for i in open("17_5.txt").readlines()]
x = y = 0
res = []
for i in a:
    if i % 19 == 0:
        res.append(i)
z = min(res)
for i in range(len(a) - 1):
    if (a[i] % z == 0) or (a[i+1] % z == 0):
            x += 1
            y = max(y, (a[i] + a[i+1]))
print(x, y)