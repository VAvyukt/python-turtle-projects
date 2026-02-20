from turtle import *

def draw_petal(x, y):
    speed(0)
    color("white")
    forward(25)
    begin_fill()
    circle(150, 40)
    left(135)
    circle(150, 40)
    end_fill()
    goto(0, 0)
    left(175)
    color("black")

# Call your commands below

bgcolor("light blue")
penup()
sety(-25)
begin_fill()
color("yellow")
circle(25)
end_fill()
goto(0, 0)
color("black")
onclick(draw_petal)
done()