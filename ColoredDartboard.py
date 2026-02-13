from turtle import *

def draw_dartboard():
    radius = 100
    penup()
    right(90)
    forward(100)
    left(90)
    for i in range(4):
        pendown()
        user_color = input("What color should this circle be: ")
        color(user_color)
        begin_fill()
        circle(radius)
        end_fill()
        radius = radius - 25
        penup()
        left(90)
        forward(25)
        right(90)

draw_dartboard()