# list = [ 4 7 21 8 -1 10 12 3]
# find all pairs whose sum is 7
# expected output: 
#     8 -1
#     4 3

# Visit each number:
#     - Put the number into a variable: x
#     - Visit numbers after this number to end of list
#           - If the sum of x and current number is 7 then print the 2 numbers (x & current number)


numbers = list(map(int, input("Enter list of numbers: ").split()))
pairSum = int(input("Enter the number for the pair sum: "))

listindex = 0 
while (listindex < len(numbers)): #listindex = 0, innerLoopIndex = 0
    x = (numbers[listindex]) #listindex = 0, innerLoopIndex = 0, x = 4
    #     - Visit numbers after this number to end of list
    innerLoopIndex = listindex + 1 #listindex = 0, innerLoopIndex = 1, x = 4
    while (innerLoopIndex < len(numbers)): #listindex = 0, innerLoopIndex = 1, x = 4
        # If the sum of x and current number is 7 then print the 2 numbers (x & current number)
        sumOfPair = x + (numbers[innerLoopIndex]) #listindex = 0, innerLoopIndex = 1, x = 4, (numbers[listindex])= 7,sumOfPair = 11
        if sumOfPair == pairSum: #listindex = 0, innerLoopIndex = 0, x = 4, (numbers[listindex])=7 ,sumOfPair = 11
            print(f"Pairs that equal 7: {x},{(numbers[innerLoopIndex])}") #listindex = 0, innerLoopIndex = 0, x = 4, (numbers[listindex])=7,sumOfPair = 11
        innerLoopIndex += 1
    listindex += 1 #listindex = 0, innerLoopIndex = 0, x = 4, (numbers[listindex])=7,sumOfPair = 11

#   0 1  2 3 4  5  6  7

# [ 4 7 21 8 -1 10 12 3]
# Output: 
# 4,3
# 8,-1

