a = open('nine_3.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    if c.count(min(c)) == 1:
        if len(list(set(c))) < len(c):
            if max(c) > 3 * ((sum(c) - max(c))/5) :
                b += 1
print(b)

