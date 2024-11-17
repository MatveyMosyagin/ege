for x in range(0, 9):
    for y in range(0, 9):
        a = int(f"88{x}4{y}", 9) + int(f"7{x}44{y}", 11)
        if a % 61 == 0:
            print(a / 61)