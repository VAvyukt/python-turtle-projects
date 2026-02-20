from turtle import *

penup()
setposition(-200, -200)

for i in range(8):
    pendown()
    circle(25)
    penup()
    forward(50)
    left(90)
    forward(50)
    right(90)