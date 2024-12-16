from itertools import *
b = '1357'
a = 0
for x in product('01234567', repeat=11):
    if x.count('1') + x.count('3') + x.count('5') + x.count('7') == 3:
        for j in x:



print(a)