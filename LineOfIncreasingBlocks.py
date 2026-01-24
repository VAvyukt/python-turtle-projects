from turtle import *

penup()
goto(-150, 0)
pendown()

length = 10

def draw_square_and_move():
    length = 10
    for i in range(5):
        for i in range(4):
            pendown()
            forward(length)
            left(90)
        penup()
        forward(length*2)
        length = length + 10
    
draw_square_and_move()