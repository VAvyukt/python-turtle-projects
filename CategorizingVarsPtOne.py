from turtle import *



# Variables to categorize (Don't alter these!)
var_1 = 10
var_2 = 'hi'
var_3 = -46.5
var_4 = '-3.14'
var_5 = 10075
var_6 = False
var_7 = 1.0
var_8 = 'True'

# Write your commands below:

penup()
#Strs Box
goto(-160, 120)
write(var_2)
goto(-160, 110)
write(var_4)
goto(-160, 100)
write(var_8)

#Ints Box
goto(60, 120)
write(var_1)
goto(60, 110)
write(var_5)

#Floats Box
goto(-150, -70)
write(var_3)
goto(-150, -80)
write(var_7)

#Bools Box
goto(60, -60)
write(var_6)

goto(0, 0)