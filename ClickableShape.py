from turtle import *

bgcolor("lightgrey")
penup()
def drawShapeSquare(x, label):
    speed(0)
    color("#388258")
    penup()
    goto(x, 120)
    pendown()
    begin_fill()
    for i in range(2):
        forward(80)
        left(90)
        forward(30)
        left(90)
    end_fill()
    penup()
    forward(3)
    left(90)
    forward(3)
    right(90)
    pendown()
    color("black")
    begin_fill()
    for i in range(2):
        forward(75)
        left(90)
        forward(25)
        left(90)
    end_fill()
    goto(x+40, 130)
    color("white")
    write(label, font=("Arial", 12), align="center")
    
def drawSquare():
    penup()
    goto(0, -20)
    backward(10)
    color("#388258")
    pendown()
    begin_fill()
    for i in range(4):
        forward(40)
        left(90)
    end_fill()
    hideturtle()
        
def drawTriangle():
    penup()
    goto(0, -20)
    backward(10)
    color("#388258")
    pendown()
    begin_fill()
    goto(30, -20)
    goto(10, 20)
    goto(-10, -20)
    end_fill()
    hideturtle()
    
def drawCircle():
    penup()
    goto(0, -20)
    color("#388258")
    pendown()
    begin_fill()
    circle(40)
    end_fill()
    hideturtle()
    
    
def drawShape(x, y):
    speed(5)
    if x <= -70:
        drawSquare()
    elif x >= 70:
        drawTriangle()
    else:
        drawCircle()

drawShapeSquare(-150, "Square")

drawShapeSquare(-40, "Circle")

drawShapeSquare(70, "Triangle")

canvas=getscreen()

canvas.onclick(drawShape)

done()