######## Utility Functions ###########

# Multiply the price per person by the number of people
def calculateBillAmount(peopleCount, pricePerPerson):
    billAmount = peopleCount * pricePerPerson
    return billAmount

# Check if the number of people is greater than 5
# If greater, then multiply the bill amount by 0.15 and then add the bill amount
# If lesser, do nothing
def addGratuity(billAmount, peopleCount):
    if peopleCount > 5:
        gratuity = billAmount * 0.15
        billAmount += gratuity
    return billAmount


def readAndValidateInputs():
    # Take number of people
    user_input1 = input("Enter number of people: ")
    peopleCount = int(user_input1)

    # Input Validation
    if (peopleCount <= 0): 
        print("Choose a valid number\n")
        return False, -1, -1

    # Take price per person
    user_input2 = input("Enter price per person: ")
    pricePerPerson = int(user_input2)

    # Input Validation
    if (pricePerPerson <= 0):
        print("Choose a valid number\n")
        return False, -1, -1
    
    return True, peopleCount, pricePerPerson

def addSalesTax(billAmount, taxRate=0.09):
    taxAmount = billAmount * taxRate
    billAmount += taxAmount
    return billAmount

###### Main program #######

while True:

    # Read and validate Inputs
    areInputsValid, peopleCount, pricePerPerson = readAndValidateInputs() 

    # If the inputs are invalid, skip next steps
    if areInputsValid == False:
        continue

    # Calculate the bill amount based on the number of people and price per person
    billAmount = calculateBillAmount(peopleCount, pricePerPerson)

    # Add gratuity (15%) as needed
    billAmount = addGratuity(billAmount, peopleCount)

    # Add sales tax @ 9%
    billAmount = addSalesTax(billAmount)

    # Print bill details: the bill amount before tax, the sales tax, and the final total
    print(f"Your total bill is: ${billAmount}\n")
