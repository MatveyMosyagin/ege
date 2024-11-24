a = open('9_9.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    list1 = []
    list2 = []
    for k in range(len(c)):
        if c.count(c[k]) == 3:
            list1.append(c[k])
        if c.count(c[k]) == 1:
            list2.append(c[k])
    if len(list1) == len(list2) == 3:
        if (sum(list1)) ** 2 > (sum(list2)) ** 2:
            b += 1
print(b)

