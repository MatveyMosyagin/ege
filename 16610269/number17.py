a = 49**10 + 7**30 - 49
b = ''
while a > 0:
    b += str(a%7)
    a = a // 7
c = b[::-1]
c = c.strip()
c = list(map(int, str(c)))
print(c.count(6))