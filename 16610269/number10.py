a = open('10_1.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    chet = []
    nechet = []
    if len(set(c)) == len(c):
        for x in c:
            if x % 2 == 0:
                chet.append(x)
            else:
                nechet.append(x)
        if len(chet) > len(nechet):
            if sum(chet) < sum(nechet):
                b += 1
print(b)