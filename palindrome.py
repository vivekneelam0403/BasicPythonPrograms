# Take user input 
# start with fIndex as 0 and bIndex as stringLength -1 
# loop while fIndex < bIndex 
    # if fIndex != bIndex 
        # print False 
        # exit program
# print True 
#__________________________________________________________________________________
 
'''
Test Cases 

Case |   Input   | Output 

1    |  racecar  |  True

2    |  none     | True 

3    |  hello    | False 

4    |  racecars | False 

5    |     a     | True 
'''
#__________________________________________________________________________________

# Code:

import sys


user_input = str(input("Enter string here: "))

def isPalindromeFunction(user_input):
    stringLength = len(user_input)

    fIndex = 0 
    bIndex = stringLength - 1 

    while fIndex < bIndex:
        if (user_input[fIndex]) != (user_input[bIndex]):
            return False
            sys.exit()
        fIndex += 1 
        bIndex -= 1
    return True

