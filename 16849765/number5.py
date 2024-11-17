res = []
for N in range(0, 1000000):
    N1 = format(N, 'b')
    if N % 5 == 0:
        N1 += format(5, 'b')
    else:
        N1 += '1'
    if int(N1, 2) % 7 == 0:
        N1 += format(7, 'b')
    else:
        N1 += '1'
    R = int(N1, 2)
    if R < 1728404:
        res.append(N)
print(max(res))

