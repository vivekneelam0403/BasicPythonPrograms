# Given a number tell whether the number is positive or not 

user_input1 = input("Enter a number: ")
number1 = int(user_input1) # Type cast string to integer
if number1 >= 0: 
    print(f"{number1} is positive")
else:
    print(f"{number1} is negative")
