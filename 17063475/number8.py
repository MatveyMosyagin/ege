from itertools import *
a = 0
chet = '0246'
nechet = '357'
for x in product(chet, nechet, chet, nechet, chet):
    if x.count('0') < 2 and x.count('2') < 2 and x.count('3') < 2 and x.count('4') < 2 and x.count('5') < 2 and x.count('6') < 2 and x.count('7') < 2:
        a += 1
for x in product(nechet, chet, nechet, chet, nechet):
    if x.count('0') < 2 and x.count('2') < 2 and x.count('3') < 2 and x.count('4') < 2 and x.count('5') < 2 and x.count('6') < 2 and x.count('7') < 2:
        a += 1
print(a)
