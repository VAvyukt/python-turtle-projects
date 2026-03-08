from turtle import *

"""
This program will let a user know if the letter they entered is the starting
or ending letter in a password.
"""


password = "mango"

for i in range(26):
    letter = input("Enter a letter: ")
    
    if password.startswith(letter):
        print("That is the first letter of the password!")
    elif password.endswith(letter):
        print("That is the last letter of the password!")
    else:
        print("That letter is not the first or last letter of the password.")