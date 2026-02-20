from turtle import *

def count_increase(x, y):
    canvas.count = canvas.count+1
    sety(0)
    color("white")
    backward(50)
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    forward(50)
    color("black")
    write(canvas.count, font=("Furtura", 25, "bold"), align="center")
    color("white")
    sety(-20)
    
speed(0)
penup()
sety(160)
write("Click Counter", font=("Furtura", 35, "bold"), align="center")
goto(0, 0)

canvas=getscreen()
canvas.count=0
write(canvas.count, font=("Furtura", 25, "bold"), align="center")
color("white")
sety(-20)
print("Please click on the canvas to increase the count. Note: if you click a lot in a short timeframe, the program may not be able to keep up with the clicks and may miss some of them. This will cause numbers to start appearing randomly and unorderly. Please click at a reasonable pace for the best experience.")
canvas.onclick(count_increase)
done()