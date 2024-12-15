def f(a, b, m):
    if a + b >= 59:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, b, m - 1), f(a * 2, b, m - 1), f(a, b + 1, m-1), f(a, b * 2, m - 1)]
    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


print(19, [s for s in range(1, 53+1) if f(5, s, 2)])
print(20, [s for s in range(1, 53+1) if not f(5, s, 1) and f(5, s, 3)])
print(21, [s for s in range(1, 53+1) if not f(5, s, 2) and f(5, s, 4)])
