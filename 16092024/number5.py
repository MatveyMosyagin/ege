result = []
for N in range(1, 10000):
    N1 = format(N, 'b')
    if N1.count('1') % 2 == 0:
        N1 += '00'
    else:
        N1 += '10'
    R = int(N1, 2)
    if R < 100:
        result.append(R)

print(max(result))