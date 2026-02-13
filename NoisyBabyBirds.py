from turtle import *

speed(0)
 # This will load the background of the program
sound = "chirp"

# Write your commands below:
speed(0)
penup()
goto(-60, 10)
write(sound.upper(), align="center", font=("Arial", 20))
goto(20, 20)
write(sound.lower(), align="center", font=("Arial", 20))
goto(95, 3)
write(sound.upper(), align="center", font=("Arial", 20))