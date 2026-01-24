from turtle import *

def draw_circle_move_down():
    radius = 25
    for i in range(4):
        penup()
        right(90)
        forward(25)
        left(90)
        pendown()
        circle(radius)
        radius = radius + 25    

draw_circle_move_down()