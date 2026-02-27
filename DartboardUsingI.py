from turtle import *

for i in range(-25, -101, -25):
    penup()
    sety(i)
    pendown()
    circle(-i)

penup()
sety(i-25)