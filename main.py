'''
Snake Water Gun Game

A simple command-line game where the user plays
against the computer.

Author: Kunal Kumar Pandey
Language: Python
'''

'''
1 for snake
-1 for water
0 for gun
'''

import random

# computer randomly chooses between snake, water, or gun
computer = random.choice([-1, 0, 1])

# user input
youstr = input("Enter your choice : ")

# mapping user input to values
youDict = {"s": 1, "w": -1, "g": 0}

# mapping values back to names
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# check for valid input
if youstr not in youDict:
    print("Invalid input! Please choose 's' for snake, 'w' for water, or 'g' for gun.")

else:
    you = youDict[youstr]

    # display choices
    print(f"You chose : {reverseDict[you]}\nComputer chose : {reverseDict[computer]}")

    # game logic
    if computer == you:
        print("It's a Draw!")

    else:
        if computer == -1 and you == 1:
            print("You Win!")

        elif computer == -1 and you == 0:
            print("You Lose!")

        elif computer == 1 and you == -1:
            print("You Lose!")

        elif computer == 1 and you == 0:
            print("You Win!")

        elif computer == 0 and you == -1:
            print("You Win!")

        elif computer == 0 and you == 1:
            print("You Lose!")

        else:
            print("Something went wrong!")
    