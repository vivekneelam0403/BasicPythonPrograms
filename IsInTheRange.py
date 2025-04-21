# Given 3 integers check whether the 1st is in the range of the other 2 numbers

user_input1 = input("Enter 1st number: ")
user_input2 = input("Enter 2nd number: ")
user_input3 = input("Enter 3rd number: ")
number1 = int(user_input1) # Type cast string to integer
number2 = int(user_input2) # Type cast string to integer
number3 = int(user_input3) # Type cast string to integer
if number1 > number2: 
    if number1 < number3:
        print(f"{number1} is in the range of {number2} and {number3}")
    else:
        print(f"{number1} is not in the range of {number2} and {number3}")
else:
    print(f"{number1} is not in the range of {number2} and {number3}")
