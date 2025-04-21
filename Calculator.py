######## Utility Functions ###########

def readInputs():
    # Takes the 1st number
    user_input1 = input("Enter the 1st number: ")
    number1 = int(user_input1)

    # Take 2nd number
    user_input2 = input("Enter the 2nd number: ")
    number2 = int(user_input2)

    # Takes the operator     
    operator = input("Enter the operator: ")

    return number1, number2, operator    


# Takes two numbers and returns the sum of two numbers
def addNumbers(number1, number2):
    return number1 + number2

# Takes two numbers and returns the difference of two numbers
def subtractNumbers(number1, number2):
    return number1 - number2

# Takes two numbers and returns the product of two numbers
def multiplyNumbers(number1, number2):
    return number1 * number2

# Takes two numbers and returns the quotient of two numbers
def divideNumbers(number1, number2):
    return number1 / number2
    
   
    

###### Main program #######


while True:

   # Take inputs: numbers and operation
    number1, number2, operator = readInputs() 

    # Calculate equation

    if operator == "+":
        #   if the operator contains "+" then add
        answer = addNumbers(number1, number2) 
    elif operator == "-":
        #   if the operator conatins "-" then substract
        answer = subtractNumbers(number1, number2) 
    elif operator == "*":
        #   if the operator contains "*" then multiply
        answer = multiplyNumbers(number1, number2) 
    elif operator == "/":
        #   if the operator contains "/" then divide
        answer = divideNumbers(number1, number2) 
    else: 
        print("Error: Unsupported Operation. Choose among +,-,*,/\n")
        continue

    # The anwser to the equation    
    print(f"Anwser to equation: {answer}\n")

