from turtle import *

def draw_eye():
    color("black")
    pendown()
    begin_fill()
    circle(10)
    end_fill()

def draw_face():
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
    draw_eye()
    penup()
    goto(30, 30)
    draw_eye()
    
def draw_smile():
    penup()
    goto(-70, -10)
    seth(270)
    pendown()
    pensize(5)
    circle(70, 180)

def draw_frown():
    penup()
    goto(70, -60)
    seth(90)
    pendown()
    pensize(5)
    circle(70, 175)
    
def draw_line():
    penup()
    goto(-70, -40)
    pendown()
    pensize(5)
    forward(130)

happy = input("Are you happy?: ")
draw_face()
if happy.lower() == "yes":
    draw_smile()
elif happy.lower() == "no":
    draw_frown()
else:
    print("Invalid Input!")
    draw_line()

done()