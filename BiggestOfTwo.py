# Given two integers, print the biggest number

user_input1 = input("Enter 1st number: ")
user_input2 = input("Enter 2nd number: ")
number1 = int(user_input1) # Type cast string to integer
number2 = int(user_input2) # Type cast string to integer
if number1 > number2: 
    print(f"{number1} is bigger than {number2}")
else: 
    print(f"{number2} is bigger than {number1}")

