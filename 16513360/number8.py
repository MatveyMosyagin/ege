a = open('number8.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    e = 0
    for x in c:
        if c.count(x) == 4:
            e = x
            if e < (sum(c) - 4*e)/3:
                print(c, e)
                b += 1
print(b/4)