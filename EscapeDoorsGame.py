#### ENGLISH ####

# Take user input on range
# If user input <= 1, print invalid # of doors
# Else, pick random integer in range of user input
# While true
    # Take user input for guess
    # If guess not in range, print, invalid input
    # If guess = rand.int, print, winner
        # Exit game
    # Else, update doorsOpened[guess] to True
    # print, try again
    # print, doorOpened
#-------------------------------------------------------------------------------------------------------------#

#### PROGRAM ####
import random
import sys

print ("Objective: Your city is being invaded by zombies, but the only way out is "
"a pathway that opens up to a room full of doors.")
print("You have to find the correct door. Good luck.")
print ()

doorsInput = int(input("Enter the amount of doors: "))

if doorsInput <= 1:
    print("Enter a number bigger than 1")
    sys.exit()

escapeDoor = random.randint(1,doorsInput)

doorsOpened = [False] * doorsInput
while True:
    guess = int(input("Pick a door to open: "))

    if guess < 1 or guess > doorsInput:
        print ("That door does not exist.")
        continue
    if guess == escapeDoor:
        print ("You have escaped!")
        break
    else:
        doorsOpened[guess-1] = True
        print("Uh Oh! Theres nothing here!")
        print ("Legend:")
        print ("T - Opened")
        print ("F - Closed")
        listindex = 0
        while (listindex < len(doorsOpened)):
            if doorsOpened[listindex] == True:
                print(f"Door {listindex + 1}: T")
            else:
                print(f"Door {listindex + 1}: F")
            listindex += 1
#-------------------------------------------------------------------------------------------------------------#

#### TESTCASES #####
# CASE 1:          #
# Input(range): 1  | 
# Output: Invalid  |
#------------------#
# CASE 2:          #
# Input(range): 5  |
# Input(guess): 2  |
# Output: Winner   |
#------------------#
# CASE 3:          #
# Input(range): 4  |
# Input(guess): 5  |
# Output: Invalid  |
#------------------#
# CASE 4:          |
# Input(range): 4  |
# Input(guess): 2  |
# Output:[F,T,F,F] |
# Input(guess): 4  |
# Output:[F,T,F,T] |
# Input(guess): 3  |
# Output:[F,T,T,T] |
# Input(guess):    |
# Output: Winner   |
#------------------#
# CASE 5:          |
# Input(range): 3  |
# Input(guess): 0  |
# Output: Invalid  |
#------------------#
#-------------------------------------------------------------------------------------------------------------#