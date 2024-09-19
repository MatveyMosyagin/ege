a = open('24.txt').readline()
res = 0
b = 3
for i in range(0, len(a) - 3):
    if a[i] == "X" and a[i + 1] == "Z" and a[i + 2] == "Z" and a[i + 3] == "Y":
        res = max(res, b)
        b = 3
    else:
        b += 1
print(res)