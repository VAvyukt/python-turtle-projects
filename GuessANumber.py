from turtle import *

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

secret_number = 3

user_number = int(input("Give me a number from 1-10 to guess the secret number: "))

while user_number != 3:
    user_number = int(input("Sorry, that isn't the secret number! Please give another guess from \n1 to 10 to guess the secret number: "))

print("Great job! That is the secret number!")
draw_green_check()