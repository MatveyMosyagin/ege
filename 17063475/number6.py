from turtle import *

tracer(0)

for i in range(8):
    right(45)
    forward(6*15)


for x in range(-25, 25):
    for y in range(-25, 25):
        up()
        goto(x*15, y*15)
        down()
        dot(5)

done()