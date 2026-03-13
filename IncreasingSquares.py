from turtle import *

def drawSquare(length):
    penup()
    right(90)
    forward(25)
    left(90)
    pendown()
    forward(length/2)
    for i in range(3):
        left(90)
        forward(length)
    left(90)
    forward(length/2)

length = 50

while length < 400:
    drawSquare(length)
    length = length + 50