import random

# Pick a random number from 0 - 1000
randomNumber = random.randint (1,1000)

def readAndValidateInputs():
# Take user input (number) 
    user_input = input("Enter a number between 1 and 1000: ") 
    number = int(user_input)

    if number > 1000:
        print ("Pick a number between 1 - 1000 \n")
        return False, -1
    elif number < 1:
        print ("Pick a number between 1 - 1000 \n")
        return False, -1
    
    return True, number

while True: 

    areInputsValid, number = readAndValidateInputs()

    if areInputsValid == False:
        continue

    # If the number is higher then print lower
    if number > randomNumber: 
        print ("Guess lower \n")
    # If the number is lower then print higher
    elif number < randomNumber: 
        print ("Guess higher \n") 
    # If the number is correct then print "You guessed the number right"
    elif number == randomNumber: 
        print ("CORRECT!!! \n") 
        exit()  
   
