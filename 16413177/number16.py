for A in range(100):
    a = 0
    for x in range(100):
        for y in range(100):
            if (3 * x + 5 * y < A) or (x >= y) or (y > 8):
                a += 1
    if a == 10000:
        print(A)
        break