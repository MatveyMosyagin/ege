a = open('11_1.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    if max(c) < sum(c) - max(c):
        if len(set(c)) == len(c):
            print(c)
            b += 1
print(b)

