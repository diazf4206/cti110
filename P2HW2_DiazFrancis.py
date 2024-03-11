#Francis Diaz

#03/10/2024

#P2HW2

#Assignment assess student understanding of Lists. Create a program that utilizes a list to track Lowes, Highest, Sum and Average of grades.

#Create an empty list to store grades
grades = [ ]

#User input for module grades to be stored in list
grades.append(float(input('Enter grade for Module 1: ')))
grades.append(float(input('Enter grade for Module 2: ')))
grades.append(float(input('Enter grade for Module 3: ')))
grades.append(float(input('Enter grade for Module 4: ')))
grades.append(float(input('Enter grade for Module 5: ')))
grades.append(float(input('Enter grade for Module 6: ')))
print()

#Display Results section
print('------------Results------------')

#Display Lowest grade from list
print(f'Lowest Grade:{min(grades):>11}')

#Display Highest grade from list
print(f'Highest Grade:{max(grades):>10}')

#Diplay sum of grades from list
print(f'Sum of Grades:{sum(grades):>11}')

#Display average of grades from list
print(f'Average:{sum(grades)/len(grades):>17.2f}')
print('----------------------------------------')
