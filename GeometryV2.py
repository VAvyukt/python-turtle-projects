from turtle import *

def draw_shapes(radius):
    for i in range(6):
        circle(radius, 360, i+1)
        radius = radius + 20

radius = 20
penup()
sety(-150)
pendown()
circle(radius)
draw_shapes(radius)