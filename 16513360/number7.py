a = open('number7.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    d = 0
    e = 0
    for x in c:
        if c.count(x) == 3 and len(set(c)) == 4:
            e = x
            if (3*e)**2 > (sum(c) - 3*e)**2:
                b += 1
                print(c)
print(b/3)

