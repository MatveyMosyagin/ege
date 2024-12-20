a = open('17.txt')
b = [int(i) for i in a]
mina = 9999
maxa = 0
count = 0
for j in range(len(b) - 1):
    if int(str(b[j])[-1]) == 5:
        mina = min(mina, b[j])
for k in range(len(b) - 1):
    if str(min(b[k], b[k + 1]))[-1] == '5' and b[k] ** 2 + b[k + 1] ** 2 < mina ** 2:
        maxa = max(maxa, b[k] ** 2 + b[k + 1] ** 2)
        count += 1
print(count, maxa)

