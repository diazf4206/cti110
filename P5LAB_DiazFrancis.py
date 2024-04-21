#Francis Diaz
#04/21/2024
#P5LAB
#Write a program that takes in a year and determines the number of days in Feb for that year

#Create function that determines the amount of days in Feb based on year
def days_in_feb(user_year):
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return 29
    else:
        return 28

#Execute user_input for year and days_print as script
if __name__ == '__main__':
    user_input = int(input())
    days_print = days_in_feb(user_input)

#Display "user_input" has "days_print" days in Feb
    print(f'{user_input} has {days_print} days in February.')

