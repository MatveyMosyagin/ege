for A in range(1000):
    a = True
    for x in range(1000):
        if not (((x & 45 > 0) or (x & 89 > 0)) <= (x & A > 0)):
            a = False
    if a:
        print(A)
        break


