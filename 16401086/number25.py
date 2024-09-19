for i in range(210235, 210300):
    a = 0
    b = []
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            a += 1
            b.append(j)
    if a == 4:
        print(b)