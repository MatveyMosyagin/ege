a = {0: "А", 1: "Г", 2: "И", 3: "Л", 4: "М", 5: "О", 6: "Р", 7: "Т"}
b = 0
for c1 in range(0, len(a)):
    for c2 in range(0, len(a)):
        for c3 in range(0, len(a)):
            for c4 in range(0, len(a)):
                b += 1
                if a[c1] == 'И' and a[c2] == 'Г':
                    print(b)
                    break