a = {0: "М", 1: "И", 2: "Т", 3: "Р", 4: "О", 5: "Ф", 6:'А', 7:'Н'}
b = f = 0
glas = 'ИОА'
soglas= 'МТРФН'
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                for c5 in range(0, len(a)):
                    for c6 in range(0, len(a)):
                        f = 0
                        r = a[c1] + a[c2] + a[c3] + a[c4] + a[c5] + a[c6]
                        if len(set(list(r))) == len(list(r)):
                            glas1 = ''
                            soglas1 = ''
                            for i in r:
                                if i in glas:
                                    glas1 += i
                                else:
                                    soglas1 += i
                            if len(soglas1) > len(glas1):
                                print(soglas1, glas1)
                                f = 0
                                for i in range(5):
                                    if (r[i] in glas and r[i+1] in glas):
                                        f = 1
                                if f == 0:
                                    b += 1
                                    print(r)

print(b)
