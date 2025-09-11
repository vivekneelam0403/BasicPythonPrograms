# Take user input
# Check for the biggest number
# Print biggest number


user_input1 = input("Enter #1: ")
user_input2 = input("Enter #2: ")
user_input3 = input("Enter #3: ")
number1 = int(user_input1)
number2 = int(user_input2)
number3 = int(user_input3)


def checkForBiggest(number1, number2, number3):
    if (number1 > number2) or (number1 > number3):
        print (f"{number1} is the biggest number")
    elif (number2 > number1) or (number2 > number3):
        print (f"{number2} is the biggest number")
    else: 
        print(f"{number3} is the biggest number")

checkForBiggest(number1,number2,number3)
