from turtle import *

def draw_star():
    seth(288)
    begin_fill()
    for i in range(5):
        forward(size) #Note: The size variable is used to control the star's size
        right(180-36)
    end_fill()

bgcolor("#D7C097")
penup()
speed(8)
size = 400

sety(size/2)
color("#E7DEAF")
draw_star()

size = size-100

sety(size/2)
color("#73AF6F")
draw_star()

size = size-100
sety(size/2)
color("#007E6E")
draw_star()