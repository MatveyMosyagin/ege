from sys import *
setrecursionlimit(1000000)


def f(x):
    if x < 11:
        return 10
    if x >= 11:
        return x + f(x - 1)


print(f(2024) - f(2022))