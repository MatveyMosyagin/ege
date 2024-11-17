a = open('9.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    if max(c)*(sum(c) - max(c) - min(c)) > (sum(c) - max(c) - min(c))*min(c) + min(c)*max(c):
        b += 1
print(b)
