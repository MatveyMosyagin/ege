a = open('18.txt')
b = [int(lines) for lines in a]
res = []
maxa = 0


for i in b:
    if i % 100 == 17 and i > maxa:
        maxa = i


for j in range(len(b) - 2):
    if (len(str(b[j])) == 4 and len(str(b[j+1])) == 4 and len(str(b[j+2])) != 4) or (len(str(b[j])) == 4 and len(str(b[j+1])) != 4 and len(str(b[j+2])) == 4) or (len(str(b[j])) != 4 and len(str(b[j+1])) == 4 and len(str(b[j+2])) == 4):
        if b[j] % 5 == 0 or b[j+1] % 5 == 0 or b[j+2] % 5 == 0:
            if b[j]+b[j+1]+b[j+2] > maxa:
                res.append(b[j] + b[j + 1] + b[j + 2])


print(len(res), max(res))