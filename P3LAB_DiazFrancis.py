#Francis Diaz
#03/09/2024
#P3LAB
# Write a program that takes in a year and determines whether that year is a leap year

is_leap_year = False
   
input_year = int(input())

if (input_year % 4 == 0) and (input_year % 100 != 0) or (input_year % 400 == 0):
    print(input_year, '- leap year')

else:
    print(input_year, '- not leap year') 
    
