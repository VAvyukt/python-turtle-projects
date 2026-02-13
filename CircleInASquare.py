from turtle import *

def draw_square(radius):
    penup()
    right(90)
    forward(radius)
    left(90)
    color("red")
    pendown()
    begin_fill()
    forward(radius)
    left(90)
    for i in range(3):
        forward(radius*2)
        left(90)
    forward(radius)
    end_fill()
    
def draw_circle(radius):
    begin_fill()
    color("blue")
    circle(radius)
    end_fill()
    
radius = int(input("What should the radius of the be: "))
draw_square(radius)
draw_circle(radius)