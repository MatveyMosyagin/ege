a = open('12_1.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    povtor = []
    for x in c:
        if c.count(x) == 2:
            povtor.append(x)
    if len(povtor) == 2 and len(set(c)) == 5:
        if sum(povtor)/2 < (sum(c) - sum(povtor))/4:
            print(c)
            b += 1
print(b)
