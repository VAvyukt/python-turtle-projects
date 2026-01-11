from turtle import *

speed(0)

def draw_circle_and_move():
    penup()
    forward(100)
    pendown()
    circle(10)
    penup()
    backward(100)
    left(10)

for i in range(36):
    draw_circle_and_move()