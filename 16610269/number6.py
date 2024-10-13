for N in range(0, 2000):
    N1 = format(N, 'b')
    N1 = N1[:-1]
    if N % 2 == 0:
        N1 += '01'
    else:
        N1 += '10'
    R = int(N1, 2)
    if R == 2018:
        print(N)
        break
