a = {0: "К", 1: "Л", 2: "Р", 3: "Т"}
b = 0
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                b += 1
                if b == 67:
                    print(a[c1], a[c2], a[c3], a[c4])