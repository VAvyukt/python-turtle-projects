from turtle import *

radius = 100

def draw_semicircle():
    cir_color = input("What color? ")
    color(cir_color)
    begin_fill()
    circle(radius, 180)
    end_fill()

penup()
setposition(0, -100)
pendown()
draw_semicircle()
draw_semicircle()