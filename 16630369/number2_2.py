a = {0: "А", 1: "В", 2: "Е", 3: "И", 4: "К", 5: "Н", 6: "О", 7: "Р"}
b = 0
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            f = a[c1] + a[c2] + a[c3]
            if f.count('В') == 1:
                b += 1
                if f.count('А') == 0:
                    print(b)
                    break