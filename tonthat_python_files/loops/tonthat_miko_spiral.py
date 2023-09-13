#---------------------------
#Programmed by: Miko Tonthat
#Date: 06/20/19
#---------------------------

#Creates a window of turtle with a Turtle named miko
import turtle
wn = turtle.Screen()
miko = turtle.Turtle()

#Input sides, lines, and percentage of increase for each arm wanted
sides = int(input("Sides wanted to draw:"))
lines = int(input("Total number of lines to draw:"))
percentage = float(input("Percentage of increase for each arm length of the spiral:"))

#Determines number of sides and size of lines
size = 10
for counter in range(lines):
    miko.forward(size)
    miko.left(360/sides)
    size = size + (size * percentage/100)

#exits the turtle program
wn.exitonclick()