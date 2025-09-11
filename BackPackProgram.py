# English
# Show backPack
    # if user chooses option 1, print backPack
# Create item 
    # if user chooses option 2, ask user: "Enter the item you want to add to the backpack:"
    # Append user input to backPack
# Delete item 
    # if user chooses option 3, print backPack and ask user: "Enter the item you want to delete
    # from the backpack"
    # Remove user input from backPack
# Quit Program
    # if user chooses option 4, then exit program
#---------------------------------------------------------------------------------------#
### Program ###
#---------------------------------------------------------------------------------------#
backPack = []

while True:
    print("____________________________________________________________________________\n")
    print("(1) Show Backpack")
    print("(2) Receive Item")
    print("(3) Deliver Item")
    print("(4) Quit Program")
    print()

    operation = int(input("Enter your choice: "))
    print()
    if operation == 1: 
        if backPack == []:
            print("There are no items in the BackPack")
            continue
        else:
            print("Your items in the BackPack are: ")
            listindex = 0
            while (listindex < len(backPack)):
                print(f"{listindex+1}. {backPack[listindex]}")
                listindex += 1
    elif operation == 2: 
        item = str(input("Enter the item you want to receive: "))
        backPack.append(item)
        print("Receiving items... ")
    elif operation == 3: 
        if backPack == []:
            print("There are no items in your BackPack")
            continue
        if item in backPack:
            item = str(input("Enter the item you want me to deliver: "))
            backPack.remove(item)
            print("Delivering item... ")
        else:
            print("Sorry that item does not exist.")
    elif operation == 4: 
        print("Quitting program...\n")
        break 
    else: 
        print("Invalid Input. Please enter a valid input")

print("Have a nice day!")
#---------------------------------------------------------------------------------------#

### Test Cases ###

# CASE 1
# Input: 2
# toys
# Input: 2
# shoes
# Input: 3
# toys
# Input: 1
# 1. shoes
# Input: 4

# CASE 2
# Input: 3
# There are no items in your BackPack
# Input: 1
# There are no items in your BackPack

# CASE 3 
# Input: 7
# Invalid Input. Please enter a valid input 
#---------------------------------------------------------------------------------------#