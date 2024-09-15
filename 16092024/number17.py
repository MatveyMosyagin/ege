a = open('17_2.txt')
x = z = 0
b = [int(i) for i in a]
for j in range(len(b) - 1):
    for k in range(j + 1, len(b)):
        if (j + k) % 120 == 0:
            x += 1
            z = max(z, j+ k)

print(x, z)