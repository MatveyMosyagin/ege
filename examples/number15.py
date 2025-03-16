#Побитовая коньюкция
# for a in range(0, 10**5):
#     k = True
#     for x in range(0, 10**5):
#         if ((x & 20777 != 0) <= ((x & 12332 == 0) <= (x & a != 0))) == 0:
#             k = False
#             break
#     if k == True:
#         print(a)
#         break

#Числовые отрезки(наибольшая длина)
# P = [i for i in range(25, 51)]
# Q = [i for i in range(32, 48)]
# m = 0
# for Amin in range(0, 100):
#     for Amax in range(Amin + 1, 100):
#         check = 1
#         A = [i for i in range(Amin, Amax)]
#         for x in range(-200, 200):
#             f = ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))
#             if not f:
#                 check = 0
#                 break
#         if check == 1:
#             m = max(m,Amax - Amin)
# print(m - 1)



#Числовые отрезки(наименьшая длина)
# list = []
# P = [i for i in range(15, 41)]
# Q = [i for i in range(21, 64)]
# for Amin in range(0, 100):
#     for Amax in range(Amin + 1, 100):
#         check = 1
#         A = [i for i in range(Amin, Amax)]
#         for x in range(-200, 200):
#             f = (x in P) <= (((x in Q) and not(x in A)) <= (not(x in P)))
#             if not f:
#                 check = 0
#                 break
#         if check == 1:
#             m = Amax - Amin
#             list.append(m)
# print(min(list) - 1)


#Координатная плоскость
# for a in range(1, 300):
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if (((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6))):
#                 k += 1
#     if k == 90_000:
#         print(a)

#Разное
def F(a, b, c):
    if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
        return 1
    else:
        return 0


for a in range(150, 0, -1):
    k = 0
    for x in range(1, 1501):
        if not ((F(x, 10, 20) == (not (max(x, 8) > 24))) and F(3, a, x)):
            k += 1
        else:
            break
    if k == 1500:
        print(a)
        break


