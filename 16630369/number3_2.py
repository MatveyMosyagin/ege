a = {0: "Е", 1: "К", 2: "М", 3: "О", 4: "П", 5: "Р", 6: "С", 7: "Т"}
b = 0
res = []
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                for c5 in range(0, len(a)):
                    b += 1
                    f = a[c1] + a[c2] + a[c3] + a[c4] + a[c5]
                    if f.count('К') == 0:
                        if f.count('Р') == 2:
                            print(f)
                            res.append(b)
print(max(res))