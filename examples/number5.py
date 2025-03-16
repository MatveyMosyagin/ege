#Первый тип заданий
# for N in range(100, 99999):
#     res = []
#     for i in range(len(str(N))-2):
#         R = str(N)[i] + str(N)[i+1] + str(N)[i+2]
#         res.append(int(R))
#     if max(res) - min(res) == 415:
#         print(N)
#         break

#Второй тип заданий
#b = '110'
def f(x, y):
    if sum(map(int,str(x))) % 2 == 0:
        y += '0'
    else:
        y += '1'
    return y

#print(f(16, b))


for N in range(123456789, 123456800):
    R = bin(N)[2:]
    print(R)
    R = f(N, R)
    R = f(int(R, 2), R)
    R = f(int(R, 2), R)
    print(int(R, 2))

