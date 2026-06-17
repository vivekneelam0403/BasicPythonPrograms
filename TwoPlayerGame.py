#### English ####
# set player1Score, player2Score to 0 
# set numberOfTurns1, numberOfTurns2 to 0
# Create new list (slots)
# while index less than 20 
    # Make each slot have a number from 0 - 1 (randomly generated)

# while true 
    # set player1pos and player2pos to 0 - 20 (randomly generated)\
    # if player1pos != player2pos, break
    # elif player1Pos == player2pos
        # generate player1pos and player2pos again 

# while true
    # while true 
        # if player1Turn != -1 or player1Turn != 1
            # print, enter a valid input 
        # else, break
    # If player1Turn = 1
        # add 1 to player1pos
    # If player1Turn does -1 at slot[x] = 0
        # print, try again  
    # If player1Turn does 1 at slot[x] = 20
        # print, try again 
    # If player1Turn =  True 
        # add however many points there are in slots[x] 
        # change slots[x] to 0 
        # add 1 to numberOfTurns1
        # print player1score, number of turns and position 
    # Repeat lines 15 to 29 for player2 
    # If numberOfTurns2 == 20
        # if player1score > player2score, print player1 is winner 
        # Repeat line 32 for player2 
        # Else, print tie 
        # sys.exit 
#-----------------------------------------------------------------------------------------------------------#

### Program ###

import random

player1Score =0 
player2Score = 0 
numOfTurns1 = 0
numOfTurns2 = 0
slots = ["Slot 1", "Slot 2", "Slot 3", "Slot 4", "Slot 5", "Slot 6", "Slot 7", "Slot 8", "Slot 9", "Slot 10","Slot 11", "Slot 12", "Slot 13", "Slot 14", "Slot 15", "Slot 16", "Slot 17","Slot 18","Slot 19", "Slot 20"]
index = 0
while index < 20:
    slots[index] = random.randint(0,1)
    index += 1

while True:
    player1pos = random.randint(0,20)
    player2pos = random.randint(0,20)
    if player1pos != player2pos:
        break
    else: 
        player1pos = random.randint(0,20)
        player2pos = random.randint(0,20)

x = 0 
while x < 5:
    while True: 
        player1Turn = int(input("Enter -1 or 1: "))
        if (player1Turn != -1) or (player1Turn != 1):
            print("Please enter a valid input")
        else: 
            break
    if player1Turn == 1: 
        player1pos += 1
    else:
        player1pos -= 1    
