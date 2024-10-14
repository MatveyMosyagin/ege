a = {0: "A", 1: "B", 2: "C", 3: "D", 4: "X", 5: "Y", 6: "Z"}
b = 0
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                        if a[c1] in 'XYZ' and a[c2] not in 'XYZ' and a[c3] not in 'XYZ' and a[c4] not in 'XYZ':
                            b += 1
print(b)