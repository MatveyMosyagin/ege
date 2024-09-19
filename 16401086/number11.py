for i in range(69, 1000):
    a = 0
    r = i * 3 - 1
    for j in range(2, (r // 2) + 1):
        if r % j == 0:
            a += 1
    if a == 0:
        print(i)
        break



