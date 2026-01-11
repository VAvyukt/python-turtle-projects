from turtle import *

speed(10)
penup()
goto(-100,-200)
pendown()
for i in range(3):
    circle(50)
    penup()
    forward(100)
    pendown()
penup()
goto(-50,-100)
pendown()
for i in range(2):
    circle(50)
    penup()
    forward(100)
    pendown()   
penup()
goto(0,0)
pendown()
circle(50)