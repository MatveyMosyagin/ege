a = open('24.txt').readline()
b = '0123456789ABCDEFGHIJKLMN'
count = 0
maxa = 0
for i in range(len(a)):
    if a[i] in b:
        count += 1
        maxa = max(count, maxa)
    else:
        count = 0

print(maxa)