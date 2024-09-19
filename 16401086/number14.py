a = 9**8 + 3**5 - 2
b = ''
while a > 0:
    b += str(a%3)
    a = a // 3
c = b[::-1]
c=c.strip()
c = list(map(int, str(c)))
print(c.count(2))