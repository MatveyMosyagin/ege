maxa = 99999999
for a in range(-200, 200):
    for b in range(a, 200):
        for x in range(-200, 200):
            if not(((a <= x <= b) <= (x**2 <= 100)) and ((x**2 <= 64) <= (a <= x <= b))):
                break
        else:
            maxa = min(maxa, b - a)
print(maxa)