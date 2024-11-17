a = open('24.txt').readline()
d = 9999999
b = []
c = 0
for i in range(len(a) - 1):
    if a[i] == "T":
        b.append(i)
for j in range(1, len(b) - 209):
    c = b[j + 209] - b[j] - 1
    if c < d:
        d = c
print(d)