#Сложение в двух системах счисления
for x in '012345678':
    for y in '012345678':
        x = str(x)
        y = str(y)
        M = int(f'88{x}4{y}', 9)
        N = int(f'7{x}44{y}', 11)
        if (int(M) + int(N)) % 61 == 0:
            print((int(M) + int(N)) // 61)


#Операции в разных СС с одной переменной
for x in '0123456789ABC':
    x = str(x)
    M = int(f'4C{x}4', 15)
    N = int(f'{x}62A', 13)
    if (int(M) + int(N)) % 121 == 0:
        print((int(M) + int(N)) // 121)


#Операции в одной СС
for x in '0123456789ABCD':
    M = int(f'123{x}5', 15)
    N = int(f'1{x}233', 15)
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













