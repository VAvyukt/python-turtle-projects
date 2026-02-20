from turtle import *

brick_length = 400 / 6
brick_height = 25

def draw_brick():
    begin_fill()
    pendown()
    for i in range(2):
        forward(brick_length)
        left(90)
        forward(brick_height)
        left(90)
    end_fill()
    penup()
    forward(brick_length)
    
penup()
backward(200)
pendown()

for i in range (2):
    color("Crimson")
    draw_brick()
    color("FireBrick")
    draw_brick()
    color("DarkRed")
    draw_brick()