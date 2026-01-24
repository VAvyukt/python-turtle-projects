from turtle import *

speed(0)

def first_triangle():
    bgcolor("#39a0ca")
    penup()
    setposition(-180, 200)
    pendown()
    color("#3c4e9d")
    begin_fill()
    goto(-60, 140)
    goto(-180, 100)
    goto(-200, 140)
    goto(-180, 200)
    end_fill()
    
def second_triangle():
    setposition(-200, 140)
    color("#364c9c")
    begin_fill()
    goto(-180, 100)
    goto(-200, 110)
    goto(-200, 140)
    end_fill()

def third_triangle():
    setposition(-180, 200)
    color("#3358a7")
    begin_fill()
    goto(-70, 200)
    goto(-60, 140)
    goto(-180, 200)
    end_fill()

def fourth_triangle():
    setposition(-70, 200)
    color("#3966b1")
    begin_fill()
    goto(-10, 200)
    goto(-60, 140)
    goto(-70, 200)
    end_fill()

def fifth_triangle():
    setposition(-60, 140)
    color("#253474")
    begin_fill()
    goto(-10, 200)
    goto(70, 200)
    goto(120, 40)
    goto(-60, 140)
    end_fill()

def sixth_triangle():
    setposition(70, 200)
    color("#123257")
    begin_fill()
    goto(180, 200)
    goto(120, 40)
    goto(70, 200)
    end_fill()

def seventh_triangle():
    setposition(180, 200)
    color("#12405e")
    begin_fill()
    goto(200, 180)
    goto(200, 70)
    goto(120, 40)
    goto(180, 200)
    end_fill()

def eighth_triangle():
    penup()
    setposition(-180, 100)
    pendown()
    color("#545ba8")
    begin_fill()
    goto(-60, 140)
    goto(-20, -10)
    goto(-180, 100)
    end_fill()

def ninth_triangle():
    setposition(-180, 100)
    color("#676199")
    begin_fill()
    goto(-20, -10)
    goto(-140, -80)
    goto(-180, 100)
    end_fill()

def tenth_triangle():
    setposition(-180, 100)
    color("#485fac")
    begin_fill()
    goto(-140, -80)
    goto(-200, -50)
    goto(-200, 110)
    goto(-180, 100)
    end_fill()

def eleventh_triangle():
    setposition(-60, 140)
    color("#3f3a6e")
    begin_fill()
    goto(120, 40)
    goto(-20, -10)
    goto(-60, 140)
    end_fill()

def twelfth_triangle():
    setposition(120, 40)
    color("#186377")
    begin_fill()
    goto(200, 70)
    goto(200, -50)
    goto(120, 40)
    end_fill()

def thirteenth_triangle():
    setposition(120, 40)
    color("#14486c")
    begin_fill()
    goto(200, -50)
    goto(200, -150)
    goto(120, -160)
    goto(120, 40)
    end_fill()

def fourteenth_triangle():
    setposition(120, 40)
    color("#242847")
    begin_fill()
    goto(120, -160)
    goto(-20, -10)
    goto(120, 40)
    end_fill()

def fifteenth_triangle():
    setposition(-20, -10)
    color("#553e57")
    begin_fill()
    goto(120, -160)
    goto(-60,-200)
    goto(-20, -10)
    end_fill()

def sixteenth_triangle():
    setposition(-20, -10)
    color("#6f6585")
    begin_fill()
    goto(-60,-200)
    goto(-140, -80)
    goto(-20, -10)
    end_fill()

def seventeenth_triangle():
    setposition(-140, -80)
    color("#4b68b1")
    begin_fill()
    goto(-60,-200)
    goto(-150, -200)
    goto(-140, -80)
    end_fill()

def eighteenth_triangle():
    setposition(-140, -80)
    color("#4169b3")
    begin_fill()
    goto(-150, -200)
    goto(-180, -200)
    goto(-200, -180)
    goto(-200, -160)
    goto(-140, -80)
    end_fill()

def nineteenth_triangle():
    setposition(-140, -80)
    color("#3b6eb6")
    begin_fill()
    goto(-200, -160)
    goto(-200, -50)
    goto(-140, -80)
    end_fill()
    
def turtle_dance():
    penup()
    seth(0)
    goto(0, 0)
    speed(8)
    for i in range(17):
        circle(10)
        forward(5)
    speed(0)

#These functions draw all of the the triangles on the mural.
first_triangle()
second_triangle()
third_triangle()
fourth_triangle()
fifth_triangle()
sixth_triangle()
seventh_triangle()
eighth_triangle()
ninth_triangle()
tenth_triangle()
eleventh_triangle()
twelfth_triangle()
thirteenth_triangle()
fourteenth_triangle()
fifteenth_triangle()
sixteenth_triangle()
seventeenth_triangle()
eighteenth_triangle()
nineteenth_triangle()

#Signing my name
penup()
seth(90)
goto(197, -195)
pendown()
color("#97d09e")
write("By: Vivaan Agrawal", font=("Georgia", 13), align="right")

#This function allows the turtle to dance in the middle before hiding.
turtle_dance()

#Hiding the turtle
penup()
color("#14486c")
forward(50)