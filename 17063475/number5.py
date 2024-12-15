for N in range(1000, 10000):
    N = str(N)
    N1 = int(N[0]) + int(N[1])
    N2 = int(N[1]) + int(N[2])
    N3 = int(N[2]) + int(N[3])
    if str(N1 + N2 + N3 - max(N1, N2, N3) - min(N1, N2, N3)) + str(max(N1, N2, N3)) == '1215':
        print(N)
        break