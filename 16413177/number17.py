def f(x):
    if x < 3:
        return 1
    if x > 2:
        a = 0
        for i in range(x):
            a += f(i)
        return a


print(f(18))