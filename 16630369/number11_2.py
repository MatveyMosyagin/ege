a = {0: "Р", 1: "О", 2: "С", 3: "О", 4: "М", 5: "А", 6:'Х', 7:'А'}
b = f = 0
glas = 'ОА'
soglas= 'РСМХ'
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                for c5 in range(0, len(a)):
                    for c6 in range(0, len(a)):
                        for c7 in range(0, len(a)):
                            for c8 in range(0, len(a)):
                                f = 0
                                r = a[c1] + a[c2] + a[c3] + a[c4] + a[c5] + a[c6] + a[c7] + a[c8]
                                if r.count('Р') == 1 and r.count('О') == 2 and r.count('С') == 1 and r.count('М') == 1 and r.count('А') == 2 and r.count('Х') == 1:
                                    for i in range(7):
                                        if (r[i] in glas and r[i + 1] in glas) or (r[i] in soglas and r[i + 1] in soglas):
                                            f = 1
                                    if f == 0:
                                        b += 1

print(b/16)