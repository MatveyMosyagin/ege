#Сложение в двух системах счисления
for x in '012345678':
    for y in '012345678':
        M = int(f'88{x}4{y}', 9)
        N = int(f'7{x}44{y}', 11)
        if (int(M) + int(N)) % 61 == 0:
            print((int(M) + int(N)) // 61)


#Операции в разных СС с одной переменной
for x in '0123456789ABC':
    M = int(f'4C{x}4', 15)
    N = int(f'{x}62A', 13)
    if (int(M) + int(N)) % 121 == 0:
        print((int(M) + int(N)) // 121)


#Операции в одной СС
for x in '0123456789ABCDEFGHIJK':
    M = int(f'82934{x}2', 21)
    N = int(f'2924{x}7', 21)
    if (M + N) % 14 == 0:
        print((M + N) // 14)
        break

#Прямое сложение в СС
a = 4**2020 + 2**2017 - 15
res = ''
while a != 0:
    res += str(a % 2)
    a //= 2
res = res[::-1]
print(res.count('1'))













