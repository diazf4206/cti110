#Francis Diaz
#03/17/2024
#PHW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
add = sum(grades)
avg = add / len(grades)

#Display Results section
print()
print('------------Results------------')

#Display Lowest grade from list
print(f'Lowest Grade:{low:>11}')

#Display Highest grade from list
print(f'Highest Grade:{high:>10}')

#Diplay sum of grades from list
print(f'Sum of Grades:{add:>11}')

#Display average of grades from list
print(f'Average:{avg:>17.2f}')
print('----------------------------------------')

# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
    print('Your grade is: B')

elif avg >=70:
    print('Your grade is: C')

elif avg >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F')










