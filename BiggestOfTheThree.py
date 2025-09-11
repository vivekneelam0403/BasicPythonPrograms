# Given 3 integers print the biggest number

user_input1 = input("Enter 1st number: ")
user_input2 = input("Enter 2nd number: ")
user_input3 = input("Enter 3rd number: ")
number1 = int(user_input1) # Type cast string to integer
number2 = int(user_input2) # Type cast string to integer
number3 = int(user_input3) # Type cast string to integer
if (number1 > number2) & (number1 > number3):
    print (f"{number1} is bigger than {number2} and {number3}")
elif (number2 > number3):
    print(f"{number2} is bigger than {number1} and {number3}")
else: 
    print(f"{number3} is bigger than {number2} and  {number1}")
