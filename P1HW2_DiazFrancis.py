#Francis Diaz
#02/25/2024
#P1HW2
#For this assignment you will create a program that does some basic math on numbers that are entered

#Display purpose of program
print('This program calculates and displays travel expenses')
print()

#Set budget amount based on user input
budg = int(input('Enter Budget: '))
print()

#Prompt for travel destination
dest = input('Enter your travel destination: ')
print()

#Set gas cost based on user input
gas = int(input('How much do you think you will spend on gas? '))
print()

#Set lodging cost based on user input
hotel = int(input('Approximately, how much will you need for accomodation/hotel? '))
print()

#Set food cost based on user input
food = int(input('Last, how much do you need for food? '))
print()

#Display travel expense section
print('------------Travel Expenses------------')

#Display location and initial budget
print('Location:', dest)
print('Initial Budget:', budg)
print()

#Display gas, hotel and food
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print()

#Display remaining balance by subtracting the sum of gas, hotel and food from budg
print('Remaining Balance:', budg - (gas + hotel + food))


