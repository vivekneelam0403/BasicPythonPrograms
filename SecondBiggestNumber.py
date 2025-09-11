# Take user input
# Initialize max and secondMax to the first element of the list
# Visit each number
#   - if number lesser than max and greater than current secondBiggest, make it secondBiggest
#   - if number greater than max, make it max, and make previous max the secondBiggest

# If number is > max

# else if number > secondMax

import sys

numbers = list(map(int, input("Enter list of numbers: ").split()))

if len(numbers) < 2:
    print("Invalid Input")
    sys.exit()

if numbers[0] > numbers[1]:
    maxNumber = numbers[0] 
    secondBiggest = numbers[1]
else:
    maxNumber = numbers[1] 
    secondBiggest = numbers[0]

listindex = 2
while(listindex < len(numbers)): # listindex = 2, maxNumber = 23, secondBiggest = 4
    if (numbers[listindex] > maxNumber):
        secondBiggest = maxNumber
        maxNumber = (numbers[listindex])
    elif (numbers[listindex] > secondBiggest):
        secondBiggest = (numbers[listindex])
    listindex += 1 # listindex = 2, maxNumber = 23, secondBiggest = 4

print(f"The second biggest number is: {secondBiggest}")

# Sample
# 0  1 2 3 
# 23 4 7 51 

# 23 4 7 5 
# max = 23
# secondBiggest = 5

