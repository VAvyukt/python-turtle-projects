from turtle import *

def move_change_bg(color_name, x, y):
    pendown()
    goto(x, y)
    bgcolor(color_name)

penup()
goto(0, -200)
bgcolor("purple")

move_change_bg("MediumOrchid", 200, 0)
move_change_bg("Magenta", 0, 200)
move_change_bg("Purple", -200, 0)
move_change_bg("MediumPurple", 0, -200)