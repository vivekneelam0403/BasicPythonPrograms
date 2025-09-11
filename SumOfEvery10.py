# TAKE USER INPUT 
# Find every 10th number in the list
# Add that number to the currentSum
# PRINT 

numbers = list(map(int, input("Enter list of numbers: ").split()))

listindex = 0 
currentSum = 0 # listindex: 4 currentSum: 22
while (listindex < len(numbers)):  # listindex: 4 currentSum: 22
#    print(numbers[listindex])
    currentSum += (numbers[listindex]) # listindex: 2 currentSum: 22
    listindex += 2 # listindex: 4 currentSum: 22

print(f"The sum of the alternate numbers in the list are: {currentSum}")

# Test Cases:

# 1 11 21 12 23 5
# Excpected: 45
# 1 40 34 2 3 4 5 
# Expected: 43
# -12 -2 0 1 
# Expected: -12
