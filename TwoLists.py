# Compare and check if two lists are the same 
# Take user input
# If list length is different
#   - Print: "Lists are different"
# Visit each number for list 1 & list 2 in parallel
#   - compare the elemts at this index. 
#   - If not same, print "not same", store isDifferent as True & stop processing
#   - if same do nothing
#   - Store in a variable: x
# If isDifferent is false
#   - Print: "Lists are different"

import sys

list1 = list(map(int, input("Enter 1st list of numbers: ").split()))
list2 = list(map(int, input("Enter 2nd list of numbers: ").split()))


if len(list1) != len(list2):
    print("Lists are different")
    sys.exit()

isDifferent = False
listindex = 0
while (listindex < len(list1)): #listindex = 0, sameNumbers = 0
    if (list1[listindex]) != (list2[listindex]):  
        print("Lists are different") 
        isDifferent = True
        break 
    listindex +=1
if isDifferent == False:
    print("Lists are same")

# Sample 1
# list1: 10, 4, 5 
# list2; 10, 3, 5
# Expected Output: "Lists are different"

# Sample 2
# list1: 10, 4, 5 
# list2; 10, 4, 5
# Expected Output: "Lists are same

# Sample 3
# list1: 10, 4
# list2: 10
# Expected Output: "Lists are different"