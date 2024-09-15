a = open('nine_2.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    d = c.sort()
    if len(set(c)) < len(c) and c.count(c[5]) == 1 and (sum(c) - sum(set(c)))*2 < c[5]:
        b += 1
print(b)