#Francis Diaz
#04/13/2024
#P4HW1
#Instead of an individual statement to collect each score, the program will use a loop. Also, after displaying score average, after dropping lowest score, the program is to display a letter grade for the calculated average


#Create Empty list for grades input by user
grades = [ ]

#Prompt user to input amount of scores they want to enter
num_scores = int(input('How many scores do you want to enter? '))

#Create for loop to prompt for input from user based on num_scores and add to list if valid
grade = 0

for i in range(num_scores):
    grade = float(input(f"Enter score #{i + 1}: "))
#Display error and repeat entry if invalid value is entered
    while not(0 <= grade <= 100): 
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        grade = float(input(f"Enter score #{i + 1} again: "))
    grades.append(grade)

#Create variable for lowest value in grades list and remove
low = min(grades)
if len(grades) > 1:
    grades.remove(min(grades))
    
#Create variable for average of values in list minus lowest value
add = sum(grades)
#If length of grades list is not divisible by 0 
if (grade == 0) and (len(grades) == 0):
    avg = 0
#If length of grades list is not divisble by 0 but grade value is > 0
elif (grade >= 1) and (len(grades) == 0):
    avg = grade
#If length of grades list is > 0 and multiple grade values exist
else:
    avg = add / len(grades)

#Display Results section
print()
print('--------------Results-----------')

#Display Lowest grade from list
print(f'Lowest Score  : {low}')

#Diplay List without lowest grade
print(f'Modified List : {grades}')

#Display average of grades from list
print(f'Scores Average: {avg:.2f}')

# determine letter grade for average
if avg >= 90:
    print('Grade         : A')

elif avg >= 80:
    print('Grade         : B')

elif avg >=70:
    print('Grade         : C')

elif avg >= 60:
    print('Grade         : D')

else:
    print('Grade         : F')
print('----------------------------------')

        
            
