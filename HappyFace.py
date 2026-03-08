from turtle import *

def draw_smiley_eye():
    color("black")
    pendown()
    begin_fill()
    circle(10)
    end_fill()

def draw_smiley_face():
    speed(0)
    penup()
    sety(-100)
    color("yellow")
    pendown()
    begin_fill()
    circle(100)
    end_fill()
    penup()
    goto(-30, 30)
    draw_smiley_eye()
    penup()
    goto(30, 30)
    draw_smiley_eye()
    penup()
    goto(-70, -10)
    seth(270)
    pendown()
    pensize(5)
    circle(70, 180)

happy = input("Are you happy?: ")
if happy.lower() == "yes":
    draw_smiley_face()
    done()