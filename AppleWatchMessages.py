from turtle import *
import random

def add_time():
    color("white")
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    if hours > 9:
        goto(30, 45)
    else:
        goto(40, 45)
    if minutes < 10:
        minutes = "0" + str(minutes)
    write(str(hours) + ":" + str(minutes), font=("Arial", 30, "bold"), align="center")
    return hours

def add_message(hour, name):
    color("#5A4B9E")
    penup()
    goto(-65, -60)
    pendown()
    begin_fill()
    for i in range(2):
        forward(130)
        circle(20, 90)
        forward(50)
        circle(20, 90)
    end_fill()
    goto(-80, 0)
    color("white")
    sleepMsg = "Time to get some rest, "
    dayMsg = "Have a lovely day, "
    afternoonMsg = "Have a wonderful afternoon, "
    eveningMsg = "Have an amazing evening, "
    if hours <= 5:
        write(sleepMsg, font=("Arial", 12))
        penup()
        sety(-20)
        write(name, font=("Arial", 12))
    elif hours in range(6, 12):
        write(dayMsg, font=("Arial", 12))
        penup()
        sety(-20)
        write(name, font=("Arial", 12))
    elif hours in range(12, 17):
        write(afternoonMsg, font=("Arial", 9))
        penup()
        sety(-20)
        write(name, font=("Arial", 12))
    else:
        write(eveningMsg, font=("Arial", 10))
        penup()
        sety(-20)
        write(name, font=("Arial", 12))
    # Complete this function to add personalized messages based on time
    
    

user_name = input("Enter the name of the watch owner: ")
hours = add_time()
add_message(hours, user_name)
done()