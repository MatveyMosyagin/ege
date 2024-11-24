for x in range(0, 8):
    for y in range(0, 8):
        a = int(f"{y}04{x}5", 11) + int(f"253{x}{y}", 8)
        if a % 117 == 0:
            print(a/117)