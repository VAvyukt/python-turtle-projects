from turtle import *

userName = input("Enter your name: ")
nameFirstLetter = input("Enter the first letter of your name: ")
print("")
print("Create an adjective aliteration with your name.")
adjective = input("Enter an adjective that starts with the first letter of your name: ")

def writeNameAliteration(adj, name):
    write(adj.capitalize()+" "+name.capitalize(), font=("Trebuchet MS", 18, "bold"), align="center")
    hideturtle()

if adjective.capitalize().startswith(nameFirstLetter.capitalize()):
    writeNameAliteration(adjective, userName)
else:
    print("The first letter of your name and the first letter of the adjective don't match")

done()