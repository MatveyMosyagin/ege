from itertools import *

def f(x, y, z, w):
    return (x <= (y == w)) and (y == (w <= z))


for a1, a2 in product([0, 1], repeat=2):
    tab = [(1, a1, 0, 1), (0, 0, a2, 0), (0, 0, 0, 1)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [1, 1, 0]:
                print(p)

