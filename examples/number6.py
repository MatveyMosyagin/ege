from turtle import *
k = 15
tracer(0)
for i in range(1):
    circle(5*k, 180)
    right(180)
    circle(-5*k, 180)



for x in range(-25, 25):
    for y in range(-25, 25):
        up()
        goto(x*k, y*k)
        down()
        dot(5)
done()