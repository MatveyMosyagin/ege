a = open('nine.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    d = c.sort()
    if (c[3] > c[1] + c[0]):
        b += 1
print(b)