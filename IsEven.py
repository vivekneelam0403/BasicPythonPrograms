# Given a number, print whether it is even or odd

user_input = input("Enter a number:")
number = int(user_input) # Type cast string to integer
remainder = number % 2
if remainder == 0: 
    print ("Even")
else: 
    print ("Odd")
  
