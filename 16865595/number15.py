import sys
sys.setrecursionlimit(999999999)


def f(n):
    if n < 15:
        return n
    if n >= 15:
        return f(n % 15) * f(n // 15)


a = 0
for x in range(1, 3**20):
    if f(x) == 7560:
        a += 1
print(a)