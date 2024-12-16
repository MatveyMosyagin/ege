a = open('25.txt').readline()
b = 0
maxa = 0
for i in range(len(a)):
    if a[i] == "Q" or a[i] == "R" or a[i] == "S":
        b += 1
    else:
        maxa = max(maxa, b)
        b = 0


print(max(maxa, b))