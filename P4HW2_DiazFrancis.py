#Francis Diaz
#04/14/2024
#P4HW2
#calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.


#Create empty dictionary to store employee pay data
emp_data = {}

#Create while loop to prompt for user input until "Done" is entered
emp_name = ''
while emp_name != 'Done':
    emp_name = input('Enter employee\'s name or "Done" to terminate: ')
    if emp_name == 'Done':
        break
    hours_worked = float(input(f'How many hours did {emp_name} work? '))
    pay_rate = float(input(f'What is {emp_name}\'s pay rate? '))
    
    # Display employee name 
    print()
    print('Employee name:  ',emp_name)
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

    #Create emp_name dictionary entries for overtime, regular and gross pay
    emp_data[emp_name] = {"otime pay": otime_pay, "reg pay": reg_pay, "gross pay": gross_pay}

    #Display Column for Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay and Gross Pay
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print('----------------------------------------------------------------------------------------')

    #Display values for Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay and Gross Pay
    print(f'{hours_worked:<15.1f}{pay_rate:<12.2f}{otime_hours:<12.1f}{otime_pay:<20.2f}${reg_pay:<20.2f}${gross_pay:.2f}')
    print()
    print()

print()

#Create variable for total number of employees in emp_data dictionary and print output
tot_emp = len(emp_data)
print('Total number of employees entered:', tot_emp)

#Create for loop to reference emp_data dictionary and calculate total overtime paid and print output
tot_otime = 0
for emp in emp_data:
    tot_otime += emp_data[emp]['otime pay']
print(f'Total amount paid for overtime: ${tot_otime:.2f}')

#Create for loop to reference emp_data dictionary and calculate total regular hour paid and print output
tot_reg = 0
for emp in emp_data:
    tot_reg += emp_data[emp]['reg pay']
print(f'Total amount paid for regular hours: ${tot_reg:.2f}')

#Create for loop to reference emp_data dictionary and cacluate total gross paid and print output
tot_gross = 0
for emp in emp_data:
    tot_gross += emp_data[emp]['gross pay']
print(f'Total amount paid in gross: ${tot_gross:.2f}')









