print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((y or z) <= (z and w)) == (not ((x and z) <= (w or y))):
                    print(x, y, z, w)