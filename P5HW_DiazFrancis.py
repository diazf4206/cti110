#Francis Diaz
#04/28/2024
#P5HW
#Create a Math Quiz with two random numbers to add and or subtract together that has a repeatable menu until ended by user

#Import randomization of numbers and define num1 and num2 as random integers from 0 to 999
import random

num1 = random.randint(0, 999)
num2 = random.randint(0, 999)

#Create function that returns num1 + num2
def add_numbers():
    return num1 + num2

#Create function that returns num1 - num2
def subtract_numbers():
    return num1 - num2

#Display Welcome to Math Quiz
print("Welcome to Math Quiz")

#Create while loop that will repeat menu until option "3" is entered
while True:
    print()
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    choice = input("Please choose one of the menu options: ")

#If option 1 is chosen, display randomnized numbers, add them together and prompt user for answer
    if choice == "1":
        print(" ", num1)
        print("+", num2)
        print()
        print("Enter answer.")
        user_answer = int(input())
        correct_answer = add_numbers()

#If option 2 is chosen, display randomnized numbers, subtract them and prompt user for answer        
    elif choice == "2":
        print(" ", num1)
        print("-", num2)
        print()
        print("Enter answer.")
        user_answer = int(input())
        correct_answer = subtract_numbers()

#If option 3 is chosen, end program  
    elif choice == "3":
        print("Thank you for playing...")
        print("Bye!!")
        break

#If invalid entry is entered, display error to user and prompt to push enter to return to Main Menu    
    else:
        print()
        print("***INVALID ENTRY***")
        print()
        print("Please choose from options 1, 2, or 3")
        input("Press 'ENTER' to return to the Main Menu")
        continue

#Create while loop that will determine how many attempts were made before right answer is entered
    guesses = 0
    while True:
        guesses += 1

#If answer is correct, display congratulation message with number of guesses        
        if user_answer == correct_answer:
            print("Congratulations!!!! Your answer is correct.")
            print("Number of guesses:", guesses)
            break

#If answer is wrong and too low, prompt user to try again        
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
            print()
            user_answer = int(input("Try again: "))

#If answer is wrong and too high, prompt user to try again             
        elif user_answer > correct_answer:
            print("Sorry, guess is too high.")
            print()
            user_answer = int(input("Try again: "))
