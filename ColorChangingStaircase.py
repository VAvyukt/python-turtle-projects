from turtle import *

penup()
goto(-200,200)
pendown()
for i in range(8):
    bgcolor("red")
    forward(50)
    right(90)
    bgcolor("green")
    forward(50)
    left(90)