a = open('nine_6.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    list1 = []
    for x in c:
        if c.count(x) == 2:
            list1.append(x)
        if c.count(x) > 2:
            break
    if len(list1) == 4 and len(set(list1)) == 2:
        if sum(list1)/4 < (sum(c) - sum(list1))/3:
            b += 1
print(b)