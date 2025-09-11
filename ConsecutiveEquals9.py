# Take user input
# Visit each number
#   - Check the consecutive 3 numbers
#   - If they equal 9, then print the numbers
#   - If they dont, do nothing

import sys

list = list(map(int, input("Enter list of numbers: ").split()))
consecutiveSum = int(input("Enter the consecutive sum: "))

if len(list) < 3:
    print("There were no three consecutive numbers that equal 9")
    sys.exit()

listindex = 0
bFound = False
while(listindex < len(list) -2): #listindex = 5, x = 7, y = 24, z = 6
    x = (list[listindex]) #listindex = 5, x = 8, y = 11, z = nothing !!
    y = (list[listindex + 1]) #listindex = 1, x = 24, y = 6, z = 6
    z = (list[listindex + 2]) #listindex = 1, x = 24, y = 6, z = 1 
    if x + y + z == consecutiveSum: #listindex = 1, x = 24, y = 6, z = 1
        print(f"The three consecutive numbers are: {x},{y},{z}")
        bFound = True
    listindex += 1 #listindex = 2, x = 24, y = 6, z = 1
if bFound == False:
    print("There were no three consecutive numbers that equal 9")


# Test case 1
# Objective: list with 9 
# 0 01 2 3 4 5 06
# 7 24 6 1 0 8 11
# Output: 1,0,8

# Testcase 2
# Objective without 9
# 4 3 1 0 1 0
# Objective: No

# Testcase 3
# Objective: negative numbers
# -1 -2 0 5 6 -9
# Output: No

# Testcase 4
# Objective: empty
# 
# Output: No

# Testcase 5
# Objective: Test a single number list
# 23
# 
# Output: No

# Testcase 6
# Objective: Test a two number list
# 23 14
# 
# Output: No

# Testcase 7
# Objective: Test a two number list
# 23 14 7
# 
# Output: No

