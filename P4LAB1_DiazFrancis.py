#Francis Diaz
#04/07/2024
#P4LAB1
#Using turtle graphics, create a square and triangle using a for or while loop

#Import turtle graphics
import turtle

#Create variable to represent turtle
franklin = turtle.Turtle()
franklin.shape("turtle")

#Draw square sides with for loop 
for i in range(4):
    franklin.color("green")
    franklin.forward(200)
    franklin.left(90)

#Move turtle to new location to draw
franklin.penup()
franklin.forward(200)
franklin.pendown()

#Draw triangle sides with for loop 
for x in range(3):
    franklin.color("red")
    franklin.forward(220)
    franklin.left(120)
