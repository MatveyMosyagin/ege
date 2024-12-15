for x in range(2030):
    a = 3**100 - x
    b = 0
    res = ''
    while a > 0:
        res += str(a % 3)
        a = a // 3
    a = res[::-1]
    if a.count('0') == 2:
        print(x)
        break

