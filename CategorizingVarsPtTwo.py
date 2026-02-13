from turtle import *



# Variables to categorize (Don't alter these!)
var_1 = 10.0
var_2 = 'hi'
var_3 = "-46.5"
var_4 = -3.14
var_5 = 100.75
var_6 = 'True'
var_7 = 1
var_8 = False

# Write your commands below:
penup()

#Strs Box
goto(-100, 100)
write((var_2), align="right")
write(str(type(var_2)))
goto(-100, 90)
write((var_4), align="right")
write(str(type(var_4)))
goto(-100, 80)
write((var_6), align="right")
write(str(type(var_6)))

#Ints Box
goto(100, 100)
write((var_7), align="right")
write(str(type(var_7)))

#Floats Box
goto(-100, -100)
write((var_1), align="right")
write(str(type(var_7)))
goto(-100, -110)
write((var_4), align="right")
write(str(type(var_4)))
goto(-100, -120)
write((var_5), align="right")
write(str(type(var_5)))

#Bools Box
goto(100, -100)
write((var_8), align="right")
write(str(type(var_8)))

goto(0, 0)