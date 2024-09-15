from turtle import *

tracer(0)

for i in range(12):
    right(60)
    forward(1*15)
    right(60)
    forward(1 * 15)
    right(270)
for x in range(-15, 10):
    for y in range(-15, 10):
        up()
        goto(x*15, y*15)
        down()
        dot(3)

done()