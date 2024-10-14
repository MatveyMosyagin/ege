a = {0: "М", 1: "А", 2: "Т", 3: "В", 4: "Е", 5: "Й"}
b = f = 0
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                for c5 in range(0, len(a)):
                    for c6 in range(0, len(a)):
                        r = a[c1] + a[c2] + a[c3] + a[c4] + a[c5] + a[c6]
                        if len(set(list(r))) == len(list(r)):
                            f = 0
                            for i in range(5):
                                if r[0] == 'Й' or (r[i] == 'А' and r[i + 1] == 'Е'):
                                    f = 1
                            if f == 0:
                                b += 1
print(b)