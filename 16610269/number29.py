a = open('24.txt').readline().split('A')
b = 0
for x in a:
    if not('B') in x and len(x) >= 8:
        b += 1
print(b)