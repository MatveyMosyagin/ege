from itertools import *

def f(x, y, z, w):
        return ((x and not y) or (x == z) or not w)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tab = [(a1, a2, 0, 0), (1, 1, 1, 0), (1, 0, a3, a4)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)