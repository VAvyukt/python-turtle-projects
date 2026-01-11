from turtle import *

speed(0)

def draw_purple_circle_and_move():
    color("purple")
    penup()
    forward(100)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()
    backward(100)
    left(10)
    
def draw_blue_circle_and_move():
    color("blue")
    penup()
    forward(100)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()
    backward(100)
    left(10)
    
def draw_red_circle_and_move():
    color("red")
    penup()
    forward(100)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()
    backward(100)
    left(10)
for i in range(12):
    draw_purple_circle_and_move()
    draw_blue_circle_and_move()
    draw_red_circle_and_move()