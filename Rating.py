from turtle import *

def draw_red_x():
    pensize(10)
    color("red")
    left(45)
    for i in range(4):
        left(90)
        forward(50)
        backward(50)
    hideturtle()
        
def draw_yellow_line():
    pensize(10)
    color("yellow")
    forward(50)
    backward(100)
    hideturtle()
    
def draw_green_check():
    pensize(10)
    color("green")
    penup()
    backward(30)
    seth(315)
    pendown()
    forward(40)
    seth(45)
    forward(85)
    hideturtle()

rating = int(input("Give me a rating from 1-10: "))

if rating <= 4:
    draw_red_x()
elif 5 <= rating <= 7:
    draw_yellow_line()
else:
    draw_green_check()

done()