a = open("17.txt")
x = 0
y = 9999999
b = [int(i) for i in a]
minb = 9999
for k in b:
    if str(k)[-1] == '5' and len(str(k)) == 3:
        minb = min(k, minb)
for j in range(len(b)-1):
        if (len(str(b[j])) == 3 and len(str(b[j+1])) != 3) or (len(str(b[j+1])) == 3 and len(str(b[j])) != 3):
            if (b[j] + b[j+1]) % minb == 0:
                x += 1
                y = min(y, b[j] + b[j+1])
print(x, y)
#Если пары идут по порядку, то один цикл и просто b[j] и b[j+1]
#Если могут быть в любом порядке, то два цикла