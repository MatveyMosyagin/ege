from itertools import *
# a = 0
# for x in product('01A', repeat = 8):
#     if x[0] != '0' and x.count('0') == 0 and x.count('A') < 5:
#         a += 1
# print(a)


# words = list(product('АОУ', repeat=5))
# print(*words[209])


# a = 0
# for x in product('ДЕКОР', repeat = 4):
#     a += 1
#     print(a, *x)
#     if x[0] == 'К':
#         print(a, *x)
#         break


# a = 0
# alf = 'КОМПЬТЕР'
# res = []
# for x in product(sorted(alf), repeat = 5):
#     a += 1
#     if x.count('К') == 0 and x.count('Р') == 2:
#         res.append(a)
# print(res)
# print(max(res))


# a = 0
# alf = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# for i in range(1, 7):
#     for x in product(sorted(alf), repeat = i):
#         a += 1
#         res = ''.join(x)
#         if res == 'FEDABC':
#             print(a)
#             break


# a = 0
# for x in product('1234', repeat = 5):
#     if x.count('1') == 2:
#         a += 1
# print(a)


# a = 0
# for x in product('01A', repeat = 8):
#     if x[0] != '0' and x.count('0') == 2 and x.count('A') <= 4:
#         a += 9**x.count('1') * 6**x.count('A')
# print(a)
#


a = 0
for x in product('0123456789AB', repeat = 5):
    if x[0] != '0' and x.count('7') == 1 and (x.count('9') + x.count('A') + x.count('B')) <= 3:
        a += 1
print(a)