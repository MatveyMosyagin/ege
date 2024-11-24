res = []
for N in range(400000000, 456789012):
    N1 = format(N, 'b')
    if N % 2 == 0:
        N1 = "11" + N1
    else:
        N1 = "1" + N1 + "10"
    res.append(int(N1, 2))
print(max(res))
