#Francis Diaz
#04/07/2024
#P4LAB1B
#Using turtle graphics, write a program that displays your first and last initials.

import turtle

#Create turtle screen with 'win' as variable
win = turtle.Screen()

#Create variable for turtle import
fd = turtle.Turtle()

#Draw letter "F" with a color of Red with pen size of 5
fd.pensize(5)
fd.color("red")
fd.setheading(90)
fd.forward(200)
fd.setheading(0)
fd.forward(125)
fd.up()
fd.goto(0,100)
fd.down()
fd.forward(70)

#Draw letter "D" with a color of Blue with pen size of 10
fd.up()
fd.goto(0,0)
fd.forward(145)
fd.setheading(90)
fd.down()
fd.pensize(10)
fd.color("blue")
fd.forward(200)
fd.setheading(0)
fd.circle(-100, 180)

#Allow for window to close with user interaction
win.mainloop()



