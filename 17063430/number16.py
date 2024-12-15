for A in range(1000):
    count = 0
    for x in range(1000):
        if ((x & 42 != 0) or (x & 13 != 0)) <= ((x & 30 == 0) <= (x & A != 0)):
            count += 1
    if count == 1000:
        print(A)
        break