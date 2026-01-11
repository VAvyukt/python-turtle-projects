from turtle import *

speed(8)
penup()
sety(-200)

def draw_square_and_move_to_pos():
    pendown()
    forward(25)
    for i in range(3):
        left(90)
        forward(50)
    left(90)
    forward(25)
    penup()
    left(90)
    forward(50)
    right(90)
    
def draw_circle_and_move_to_pos():
    pendown()
    circle(25)
    penup()
    left(90)
    forward(50)
    right(90)

for i in range(4):
    draw_square_and_move_to_pos()
    draw_circle_and_move_to_pos()