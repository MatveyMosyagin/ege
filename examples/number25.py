# from fnmatch import *
#
# for x in range(0, 10 ** 10, 2024):
#     if fnmatch(str(x), '3?6906*4'):
#         print(x)



# for x in range(201455, 201470+1):
#     list = []
#     for i in range(1, x+1):
#         if x % i == 0:
#             list.append(i)
#     if len(list) == 4:
#         # list.remove(1)
#         # list.remove(x)
#         print(list, x)


a = []
for m in range(0, 30, 2):
    for n in range(1, 20, 2):
        x = 2 ** m * 3 ** n
        if 400000000 <= x <= 600000000:
            a.append(x)
print(*sorted(a))

