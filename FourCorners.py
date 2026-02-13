from turtle import *

def draw_square():
    pendown()
    for i in range(4):
        forward(side_length)
        right(90)
    penup()

user_name = input("Type your name here: ")
msg = "Hi {}! Welcome to Four Corners!"
print(msg.format(user_name))
side_length = int(input("What should be the length of each side of the squares: "))
penup()
goto(-200, 200)
draw_square()
seth(270)
goto(200, 200)
draw_square()
seth(90)
goto(-200, -200)
draw_square()
seth(180)
goto(200, -200)
draw_square()