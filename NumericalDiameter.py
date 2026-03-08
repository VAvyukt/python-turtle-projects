from turtle import *

diameter = input("Enter a diameter for the circle: ")

while diameter.isdigit() == False:
    print("Invalid Response Entered! Pleae enter ONLY a numeric value.")
    diameter = input("Enter a diameter for the circle: ")
    
if diameter.isdigit() == True:
    circle(int(diameter)/2)