def f(x):
    if x >= 2000:
        return 2000
    if x < 2000 and x % 2:
        return x * f(x + 1)
    else:
        return x * (f(x + 1) // 2)


print(f(1998) / f(2001))