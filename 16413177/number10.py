a = open('nine_5.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    if len(set(c)) == len(c):
        if (max(c) + min(c))/2 > (sum(c) - min(c) - max(c))/4:
            b += 1
print(b)