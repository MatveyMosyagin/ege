import sys
sys.setrecursionlimit(100000)


def f(x):
    if x == 1:
        return 1
    if x > 1:
        return x - 2 + f(x-1)


print(f(2023) - f(2021))


