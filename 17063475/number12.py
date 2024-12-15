mina = 100000
for x in range(1000):
    for y in range(1000):
        a = '0' + '1' * x + '2' * y
        if len(a) > 44:
            while '01' in a or '02' in a:
                if '02' in a:
                    a = a.replace('02', '1110', 1)
                if '01' in a:
                    a = a.replace('01', '220', 1)
            for j in range(2, (a.count('1') + a.count('2') * 2)):
                flag = 0
                if (a.count('1') + a.count('2') * 2) % j == 0:
                    flag = 1
                    break
                if flag == 0:
                    mina = min(mina, x + 2 * y)
print(mina)