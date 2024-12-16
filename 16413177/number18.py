a = open("18.txt")
b = [int(i) for i in a]
count = 0
res = []
maxa = 999999999
for i in b:
    if len(str(i)) >= 2 and str(i)[-2:] == '24':
        res.append(i)


for j in range(len(b) - 2):
    if (len(str(b[j])) == 3 and len(str(b[j + 1])) != 3 and len(str(b[j + 2])) != 3) or (len(str(b[j])) != 3 and len(str(b[j + 1])) == 3 and len(str(b[j + 2])) != 3) or (len(str(b[j])) != 3 and len(str(b[j + 1])) != 3 and len(str(b[j + 2])) == 3):
        if b[j] + b[j + 1] + b[j + 2] > max(res):
            maxa = min(maxa, b[j] + b[j + 1] + b[j + 2])
            count += 1
print(count, maxa)
