from turtle import *

def move_and_label(x, y):
    penup()
    goto(x, y)
    label = "x: {}, y: {}"
    write(label.format(x, y), align="center")
    
screen = getscreen()
screen.onclick(move_and_label)
done()