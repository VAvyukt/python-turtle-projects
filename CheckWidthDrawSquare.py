from turtle import *

def check_for_number(userLength):
    while userLength.isdigit() != True:
        userLength = input("Not a valid length! Please enter a numeric value for the side length of the square: ")
    userLength = int(userLength)
    return userLength

def drawSquare(userLength):
    for i in range(4):
        forward(userLength)
        left(90)

userLength = input("Please enter a number to be used for the square length: ")
userLength = check_for_number(userLength)
drawSquare(userLength)
done()