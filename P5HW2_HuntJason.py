#This project displays random numbers that have to be added or subtracted by the user.
#11/27/2022
#CTI-110 P5HW2 - Math Quiz
#Jason Hunt
# Display user options
# Get users option to 1 add random numbers, 2 subtract random numbers, or 3 to end the program.
# generate random numbers
# Get users answer and calc if they are correct, to low, to high, and how many inputs the user had

import random

print("Welcome to Math Quiz")
print("")

def add_random():
    number_1=random.randint(0,100)
    number_2=random.randint(0,100)
    print(f"{number_1:>6}")
    print(f"+{number_2:>5}")
    print("\nEnter answer.")
    ans = int(input())

    count = 1
    while ans != number_1 + number_2:
        if ans < number_1 + number_2:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

        ans = int(input("\nTry again: "))
        count = count + 1
    print("Congradulations!!!! your answer is correct..")
    print("Number of guesses: ", count)

def sub_random():
    number_1=random.randint(0,100)
    number_2=random.randint(0,100)
    print(f"{number_1:>6}")
    print(f"-{number_2:>5}")
    print("\nEnter answer.")
    ans=int(input())
    
    count = 1
    while ans != number_1 - number_2:
        if ans < number_1 - number_2:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")
        
        ans = int(input("\nTry again: "))
        count = count + 1 
    print("Congradulations!!!! your answer is correct..")
    print("Number of guesses: ", count)
    
if __name__ == "__main__":

    while 1:
        print("\nMAIN MENU")
        print("--------------")
        print("1) Adding Random Numbers")
        print("2) Subtracting Random Numbers")
        print("3) Exit")
        num = int(input("Please choose one of the menu options: "))

        if num == 1:
            add_random()
        elif num == 2:
            sub_random()
        elif num == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Enter correct number.")
        
        
