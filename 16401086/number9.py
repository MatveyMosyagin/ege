a = open('nine_3.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    list1 = []
    list2 = []
    for x in c:
        if c.count(x) == 1:
            list1.append(x)
        else:
            list2.append(x)
    if (len(list1) > 0) and (len(list2) > 0):
        if sum(list1)/len(list1) > sum(list2)/len(list2):
            b += 1

print(b)