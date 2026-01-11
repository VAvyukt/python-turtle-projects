from turtle import *

def draw_square():
    pendown()
    color("red")
    begin_fill()
    circle(60, 360, 4)
    end_fill()
    penup()
    
def draw_circle():
    pendown()
    color("blue")
    begin_fill()
    circle(60)
    end_fill()
    penup()

def draw_semicircle():
    pendown()
    color("yellow")
    begin_fill()
    circle(60, 180)
    end_fill()
    penup()
    
def draw_pentagon():
    pendown()
    color("green")
    begin_fill()
    circle(60, 360, 5)
    end_fill()
    penup()

bgcolor("tan")
penup()
goto(-100,40)
draw_square()
goto(100,40)
draw_circle()
goto(-120,-160)
draw_semicircle()
goto(100,-160)
seth(0)
draw_pentagon()