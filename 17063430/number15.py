res = []
for x in "0123456789AB":
    for y in "0123456789AB":
        a = int(f"{x}231{y}", 12) + int(f"78{x}98{y}", 14)
        if a % 99 == 0:
            res.append(a)
print(min(res) / 99)