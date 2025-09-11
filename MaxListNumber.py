# Find the highest number in the list
# Take user input
# Check if the number is bigger than the biggest number so far 
# Print the biggest number

numbers = list(map(int, input("Enter list of numbers: ").split()))

def biggestOfTwoNumbers(number1, number2):
    if (number1 > number2):
        return number1
    else:
        return number2
    
listindex = 0 
biggestNumber = numbers[0] # listindex=0, biggestNumber = 2
while (listindex < len(numbers)):  # listindex=3, biggestNumber = 4
    #    print (numbers[listindex])
    # Check if the number is bigger than current biggest number 
        # If the number is bigger make it the current biggest number
        # If not do nothing
    
    biggestNumber = biggestOfTwoNumbers((numbers[listindex]), biggestNumber)

    listindex += 1 # listindex=3, biggestNumber = 45 

# Print the biggest number
print (f"The biggest number in the list is: {biggestNumber}")

# Given a list of number, print only the prime numbers
# Check if number is only divisible by 1 (primeNumbers)
# Print (primeNumbers)

# Given a list of number, print only the prime numbers
# For each number in the list
#   - If it is a prime number, print that number
#   - If it's not a prime number, do nothing


def isPrime(number):
    # Check whether the number is divible by 2,3,4,5... until number-1
    # If that number was divisble by any of the above, it's not a prime
    # If not, that number is a prime

    index=2
    while (index < number-1):
        if (number%index == 0):
            return False
        index += 1

    return True

listindex = 0 
while (listindex < len(numbers)):
    isPrimeNum = isPrime((numbers[listindex]))
    if isPrimeNum == True: 
        print (f"{numbers[listindex]} is a prime number")
    listindex += 1

# Can you practive enough to be able to solve problems like isPrime & 
# be able to use functions like this !!




