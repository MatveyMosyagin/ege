a = {0: "А", 1: "Б", 2: "З", 3: "И"}
b = 0
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                b += 1
                if c1 == 3 and c2 == 2 and c3 == 1 and c4 == 0:
                    print(b)