from turtle import *

radius = 100
penup()
setposition(0, -100)
pendown()
for i in range(3):
    circle(radius)
    radius = radius / 2