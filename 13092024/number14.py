res = []
for x in "0123456789ABC":
    a = int(f"26{x}98", 13) + int(f"4{x}296", 13)
    if a % 34 == 0:
        print(a // 34)
        break