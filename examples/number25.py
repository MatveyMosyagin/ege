# from fnmatch import *
#
# for x in range(0, 10 ** 11, 154682):
#     if fnmatch(str(x), '*192?3*68'):
#         print(x, x//154682)



def f(x):
    a = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)
    return sum(a)


for j in range(500000, 500100):
    if f(j) % 10 == 6:
        print(j, f(j))

