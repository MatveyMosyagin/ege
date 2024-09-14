a = open('17.txt')
x = y = z = 0
b = [int(i) for i in a]
for j in range(len(b) - 1):
    for k in range(j + 1, len(b)):
        if min(j, k) % 10 == 5 and (j**2 + k**2) < max(y, min(b[j], b[k])):
            x += 1
            z = max(z, k**2 + j**2)

print(x, z)