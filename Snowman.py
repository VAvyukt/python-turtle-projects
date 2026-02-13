from turtle import *

def bottom_snowball(radius):
    penup()
    sety(-200)
    color("white")
    pendown()
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(radius*2)
    right(90)
    
def middle_snowball(radius):
    pendown()
    begin_fill()
    circle(radius/2)
    end_fill()
    penup()
    left(90)
    forward((radius/2)*2)
    right(90)
    
def top_snowball(radius):
    pendown()
    begin_fill()
    circle((radius/2)/2)
    end_fill()
    penup()
    left(90)
    forward(((radius/2)/2)*2)
    right(90)

bgcolor("#DBF4FA")
bottom_radius = int(input("What should the radius of the bottom snowball be (10-100): "))
bottom_snowball(bottom_radius)
middle_snowball(bottom_radius)
top_snowball(bottom_radius)