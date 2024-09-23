for a in range(100, 1000):
    a = str(a)
    b1 = int(a[0]) + int(a[1])
    b2 = int(a[2]) + int(a[1])
    c = str(min(b1, b2)) + str(max(b1, b2))
    if c == '714':
        print(a)
        break