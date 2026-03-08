from turtle import *

side_length = 20
space = 10
count = 0
def draw_square():
    if (count % 2) == 0:
        pendown()
        begin_fill()
        for i in range(4):
           forward(side_length)
           left(90)
        end_fill()
        penup()
        forward(space + side_length)
    else:
        for i in range(4):
            pendown()
            forward(side_length)
            left(90)
        penup()
        forward(space + side_length)

penup()
setx(-90)
for i in range(6):
    draw_square()
    count = count + 1