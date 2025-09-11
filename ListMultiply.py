# TAKE USER INPUT
# Multiply each number by 2
# PRINT EACH NUMBER

numbers = list(map(int, input("Enter list of numbers: ").split()))

listindex = 0  # listindex: 1,  numbers = [2,5,2]
while (listindex < len(numbers)): # listindex: 1, numbers [2,5,2]
   numbers[listindex] = (numbers[listindex])*2 #listindex: 0 numbers: [2,5,2] 
   listindex += 1 #listindex: 1, numbers = [2,5,2]

print (f"The Modified list is: {numbers}")

# Test Cases
# 1 5 2 
# Expected: 2 10 4
# -1 0 10
# Expected: -2 0 20
# 2 4 6 
# Expected: 4 8 12
