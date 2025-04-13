# a = open('9.txt')
# count = 0
# for i in a:
#     b = [int(j) for j in i.split()]

a = open('9.txt')
count = 0
for i in a:
    b = [int(j) for j in i.split()]
    chet = []
    nechet = []
    zametchet = []
    zametnechet = []
    for k in range(0, len(b)):
        if b[k] > sum(b)/8 and b[k] % 2 == 0:
            zametchet.append(b[k])
        if b[k] > sum(b)/8 and b[k] % 2 == 1:
            zametnechet.append(b[k])
        if b[k] % 2 == 0:
            chet.append(b[k])
        if b[k] % 2 == 1:
            nechet.append(b[k])
    if len(zametchet) > len(zametnechet) and sum(chet) < sum(nechet):
        count += 1
print(count)