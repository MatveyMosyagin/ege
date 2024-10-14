a = {0: "А", 1: "Г", 2: "М", 3: "Н", 4: "С", 5: "Т", 6: "У"}
b = 0
res = []
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                for c5 in range(0, len(a)):
                    for c6 in range(0, len(a)):
                        f = a[c1] + a[c2] + a[c3] + a[c4] + a[c5] + a[c6]
                        b += 1
                        if f[0] != 'У' and f.count('М') == 2 and f.count('Г') < 2:
                            res.append(b)
print(max(res))