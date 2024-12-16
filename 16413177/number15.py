for x in "0123456789AB":
    a = int(f"28{x}2", 18) + int(f"93{x}5", 12)
    if a % 133 == 0:
        print(a//133)