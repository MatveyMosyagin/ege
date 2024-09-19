res = []
for a in range(1000, 10000):
    a = (list(map(int, str(a))))
    if a[0]+a[1] > a[2] + a[3]:
        a1 = str(a[2] + a[3]) + str(a[0] + a[1])
    else:
        a1 = str(a[0] + a[1]) + str(a[2] + a[3])
    if a1 == '616':
        res.append(a1)


print(len(res))