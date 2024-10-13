for A in range(100):
    a = 0
    for x in range(100):
        for y in range(100):
            if (x < A) or (y < A) or ((x + 2*y) > 50):
                a += 1
    if a == 10000:
        print(A)
        break