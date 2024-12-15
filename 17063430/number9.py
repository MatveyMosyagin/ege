from itertools import *
count = 0
nechet = "1357"
chet = "2468"
for x in product(nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet):
    if x.count(x[0]) <= 4 and x.count(x[1]) <= 4 and x.count(x[2]) <= 4 and x.count(x[3]) <= 4 and x.count(x[4]) <= 4 and x.count(x[5]) <= 4 and x.count(x[6]) <= 4 and x.count(x[7]) <= 4 and x.count(x[8]) <= 4 and x.count(x[9]) <= 4 and x.count(x[10]) <= 4:
        count += 1

for x in product(chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet, nechet, chet):
    if x.count(x[0]) <= 4 and x.count(x[1]) <= 4 and x.count(x[2]) <= 4 and x.count(x[3]) <= 4 and x.count(x[4]) <= 4 and x.count(x[5]) <= 4 and x.count(x[6]) <= 4 and x.count(x[7]) <= 4 and x.count(x[8]) <= 4 and x.count(x[9]) <= 4 and x.count(x[10]) <= 4:
        count += 1


print(count)
