from turtle import *

circle_color = "red"
circle_radius = 50
square_color = "blue"
square_width = circle_radius * 2

penup()
goto(-100, 0)
color(circle_color)
begin_fill()
circle(circle_radius)
end_fill()
goto(-100, -20)
color("black")
write(str(circle_color) + " circle with radius of  " + str(circle_radius), align="center")

goto(50, 0)
color(square_color)
begin_fill()
for i in range(4):
    forward(square_width)
    left(90)
end_fill()
goto(100, -20)
color("black")
write(str(square_color) + " square with width of  " + str(square_width), align="center")

goto(0, -100)