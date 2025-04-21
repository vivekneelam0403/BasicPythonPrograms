## Given a number, return true if it is a multiple of three, otherwise false

user_input = input("Enter a number: ")
number = int(user_input) # Type cast string to integer
remainder = number % 3
if remainder == 0: 
    print ("Multiple Of Three")
else: 
    print ("Not a multiple of three")
