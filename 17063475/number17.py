a = open('17.txt')
b = [int(i) for i in a]
res = []
maxa = 0
for j in b:
    if j % 1000 == 123 and j > maxa:
        maxa = j
for i in range(len(b) - 2):
    if (b[i] + b[i + 1] + b[i + 2]) > maxa:
        if ((b[i] % 3 == 0) + (b[i + 1] % 3 == 0) + (b[i + 2] % 3 == 0)) == 1:
            if len(str(b[i])) == 5 and len(str(b[i + 1])) == 5 or len(str(b[i + 2])) == 5 and len(str(b[i + 1])) == 5 or len(str(b[i + 2])) == 5 and len(str(b[i])) == 5:
                res.append(b[i] + b[i + 1] + b[i + 2])
print(len(res), max(res))