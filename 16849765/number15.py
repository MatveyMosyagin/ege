for A in range(100):
    a = 0
    for x in range(100):
        if ((x & 25 == 0) or (x & 17 != 0) or (x & A != 0)) == 0:
            a = 1
    if a == 0:
        print(A)
        break