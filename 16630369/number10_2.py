a = {0: "Г", 1: "Е", 2: "Р", 3: "А", 4: "С", 5: "И", 6:'М'}
b = f = 0
glas = 'ЕАИ'
soglas= 'ГРСМ'
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                for c5 in range(0, len(a)):
                    for c6 in range(0, len(a)):
                        for c7 in range(0, len(a)):
                            r = a[c1] + a[c2] + a[c3] + a[c4] + a[c5] + a[c6] + a[c7]
                            if len(set(list(r))) == len(list(r)):
                                f = 0
                                for i in range(6):
                                    if (r[i] in glas and r[i+1] in glas) or (r[i] in soglas and r[i+1] in soglas):
                                        f = 1
                                if f == 0:
                                    b += 1
print(b)