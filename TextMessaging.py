from turtle import *



# Text from Haley
text_1 = "omg"
# Text from Haley
text_2 = "the funniest thing happened"
# Text from me
text_3 = "what"
# Text from Haley
text_4 = "i farted in math class"
# Text from me
text_5 = "haha"

penup()

color("lightgreen")
goto(90, 100)
write(text_1.upper(), font=("Arial", 10), align="right")
goto(90, 70)
write(text_2.capitalize() + ".", font=("Arial", 10), align="right")

color("lightblue")
goto(-90, 10)
write(text_3.capitalize() + "?", font=("Arial", 10))

color("lightgreen")
goto(90, -50)
write(text_4.capitalize() + "!", font=("Arial", 10), align="right")

color("lightblue")
goto(-90, -110)
write(text_5.upper() + text_5.upper() + "!!", font=("Arial", 10))

goto(0, -200)