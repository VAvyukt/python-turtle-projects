from turtle import *

def draw_textbox(label, y_location):
    goto(-50, y_location)
    write(label, font=("Arial", 15, "bold"), align="right")
    forward(5)
    pendown()
    for i in range(2):
        forward(200)
        left(90)
        forward(25)
        left(90)
    penup()
    goto(-40, y_location + 5)
    
def draw_availability(label, y_location):
    goto(60, y_location)
    write(label, font=("Arial", 15), align="right")
    forward(5)
    pendown()
    for i in range(2):
        forward(50)
        left(90)
        forward(25)
        left(90)
    penup()
    goto(80, y_location + 5)

speed(0)
bgcolor("#DBF4FA")
print("Welcome to the volunteer sign up form!")

penup()
draw_textbox("Name:", 150)
user_name = input("Enter your name: ")
write(str(user_name), font=("Georgia", 16), align="left")

msg= "Nice to meet you, {}"
print(msg.format(user_name))

draw_textbox("Date:", 100)
print("")
date = input("Enter today's date (mm/dd/yyyy): ")
write(str(date), font=("Georgia", 16), align="left")

draw_textbox("Grade:", 50)
print("")
print("You must be in middle or high school to volunteer.")
grade = input("Enter your grade level (only number): ")
write(str(grade + "th"), font=("Georgia", 16), align="left")

goto(-150, 0)
pensize(5)
pendown()
goto(150, 0)
pensize(1)
penup()
goto(-75, -50)

write("Availability:", font=("Arial", 23, "bold"), align="left")
print("")

print("Now let's look at your availability. Enter 'Y' if available during the given time and 'N' if you are not.")
avail_msg = "Are you available {}s? (Y/N): "

draw_availability("Saturday Morning:", -100)
sat_mor = input(avail_msg.format("Sat morning"))
write(str(sat_mor), font=("Georgia", 16), align="left")

draw_availability("Saturday Afternoon:", -130)
sat_aft = input(avail_msg.format("Sat afternoon"))
write(str(sat_aft), font=("Georgia", 16), align="left")

draw_availability("Sunday Morning:", -160)
sun_mor = input(avail_msg.format("Sun morning"))
write(str(sun_mor), font=("Georgia", 16), align="left")

draw_availability("Sunday Afternoon:", -190)
sun_aft = input(avail_msg.format("Sun afternoon"))
write(str(sun_aft), font=("Georgia", 16), align="left")

print("")
thank_you_msg = "Awesome, thank you for filling out the volunteer form, {}!"
print(thank_you_msg.format(user_name))
print("We will be in touch.")