a = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6:'6', 7:'7'}
b = f = 0
nechet = '1357'
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                for c5 in range(0, len(a)):
                    f = 0
                    r = a[c1] + a[c2] + a[c3] + a[c4] + a[c5]
                    if a[c1] != '0' and r.count('6') == 1:
                        for i in range(4):
                            if (r[i] in nechet and r[i + 1] == "6") or (r[i + 1] in nechet and r[i] == "6"):
                                f = 1
                        if f == 0:
                            b += 1

print(b)