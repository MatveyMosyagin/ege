def f(a, m):
    if a <= 17:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a - 1, m - 1)]
    if a % 3 == 0:
        h.append(f(a // 3, m - 1))
    else:
        h.append(f(a - 2, m - 1))
    if a % 5 == 0:
        h.append(f(a // 5, m - 1))
    else:
        h.append(f(a - 3, m - 1))
    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


print(19, [s for s in range(18, 100) if not f(s, 1) and f(s, 2)])
print(20, [s for s in range(18, 100) if not f(s, 1) and f(s, 3)])
print(21, [s for s in range(18, 100) if not f(s, 2) and f(s, 4)])
