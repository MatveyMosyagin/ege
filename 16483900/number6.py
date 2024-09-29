res = []
for N in range(0, 1000):
    N1 = format(N, 'b')
    if N % 2 == 0:
        N2 = N1 + '10'
    else:
        N2 = N1 + '01'
    R = int(N2, 2)
    if R < 102:
        res.append(R)
print(max(res))