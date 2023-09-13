#-----------------------------
#Programmed by: Miko Tonthat
#Date: 06/20/19
#-----------------------------

#Creates a window of turtle with 2 Turtles named miko and tonthat
import turtle
wn = turtle.Screen()

#Determines how miko, the turtle, will be like
miko = turtle.Turtle()
miko.up()
miko.shape("square")

#Determines how tonthat, the Turtle, will be like
tonthat = turtle.Turtle()
tonthat.down()

#Creates the clock
for hours in range(12):
    miko.forward(150)
    miko.stamp()
    miko.backward(150)
    miko.left(360/12)
    
#Integrates computer time into the turtle program
import datetime
hour = datetime.datetime.now().hour % 12
minute = datetime.datetime.now().minute
minute_hand_angle = minute * 6 - 90
hour_hand_angle = (hour + (minute / 60)) * 30 - 90

#Creates hour hands
tonthat.right(hour_hand_angle)
tonthat.forward(100)
tonthat.home()

#Creates minute hands
tonthat.right(minute_hand_angle)
tonthat.forward(120)
tonthat.home()

#Exits the turtle program when clicked
wn.exitonclick()