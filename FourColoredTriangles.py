from turtle import *

penup()
setx(-100)
pensize(5)

def draw_triangle_and_move_to_pos():
    color("red")
    pendown()
    forward(50)
    left(120)
    color("blue")
    forward(50)
    left(120)
    color("green")
    forward(50)
    penup()
    left(120)
    forward(50)
    
for i in range(4):
    draw_triangle_and_move_to_pos()