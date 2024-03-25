#Francis Diaz

#03/24/2024

#P3HW2

#Create a program that calculates salary based on pay rate, hours worked and over time per week

#Prompt for input by user for Employee Name, Hours Worked and Pay Rate
emp_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter empoyee's pay rate: "))
print('-----------------------------------')

#Diplay Employee's name
print('Employee name: ',emp_name)
print()

#Calculate Overtime Pay Rate:
otime_rate = pay_rate * 1.5

#Calculate Overtime Hours:
otime_hours = hours_worked - 40

if hours_worked <= 40:
    otime_hours = 0

#Calculate Overtime Pay
otime_pay = otime_hours * otime_rate

#Calculate RegHour Pay
reg_pay = hours_worked * pay_rate

if hours_worked > 40:
    reg_pay = (hours_worked - otime_hours) * pay_rate
    
#Calculate Gross Pay
gross_pay = reg_pay + otime_pay

#Display Column for Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay and Gross Pay
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
print('--------------------------------------------------------------------------------------------------')

#Display values for Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay and Gross Pay
print(f'{hours_worked:<15.1f}{pay_rate:<12.1f}{otime_hours:<12.1f}{otime_pay:<20.2f}${reg_pay:<20.2f}${gross_pay:.2f}')













