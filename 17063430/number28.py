a = open('24.txt').readline()
b = 0
maxa = 0
for i in range(len(a)):
    if a[i] == "B" and b == 0:
        b += 1
    elif b > 0 and (a[i] in "123456" or ((a[i] in "-*") and (a[i-1] not in "-*"))):
        b += 1
    else:
        maxa = max(maxa, b)
        b = 0
print(max(maxa, b))