from turtle import *

tracer(0)

for i in range(4):
    forward(12*15)
    right(90)
for i in range(5):
    forward(4*15)
    right(45)


for x in range(-25, 25):
    for y in range(-25, 25):
        up()
        goto(x*15, y*15)
        down()
        dot(5)

done()