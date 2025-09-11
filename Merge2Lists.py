# English
# Take user input
# Visit each number in list1 and list2
    # If list1[index1] > list2[index2], append list1[index1] to sortedList
    # If list1[index1] = list2[index2], append both to sortedList
    # Else, append list2[index2]
# If index1 != length of list1, append remaining numbers to sortedList and print
# If index2 != length of list2, append remaining numbers to sortedList and print
# Else, print sortedList
#---------------------------------------------------------------------------------------------#

# Program

list1 = list(map(int, input("Enter 1st list of numbers: ").split()))
list2 = list(map(int, input("Enter 2nd list of numbers: ").split()))

listIndex1 = 0
listIndex2 = 0
sortedList = []

while (listIndex1 < len(list1)) and (listIndex2 < len(list2)):
    if list1[listIndex1] < list2[listIndex2]:
        sortedList.append(list1[listIndex1])
        listIndex1 += 1
    elif list2[listIndex2] < list1[listIndex1]:
        sortedList.append(list2[listIndex2])
        listIndex2 += 1
    else: 
        sortedList.append(list1[listIndex1])
        sortedList.append(list2[listIndex2])
        listIndex2 += 1
        listIndex1 += 1

if listIndex1 != len(list1):
    while (listIndex1 < len(list1)):
        sortedList.append(list1[listIndex1])
        listIndex1 += 1
elif listIndex2 != len(list2):
    while (listIndex2 < len(list2)):
        sortedList.append(list2[listIndex2])
        listIndex2 += 1

print(f"Your sorted list is: {sortedList}")
#---------------------------------------------------------------------------------------------#

# Testcases:

# Case 1:
# Inputs: (1,2,3) (2,3,4)
# Outputs: 1,2,2,3,3,4
#---------------------------------------------------------------------------------------------#
# Case 2:
# Inputs: (5,7,9) (8,10,12)
# Outputs: 5,7,8,9,10,12
#---------------------------------------------------------------------------------------------#
# Case 3:
# Inputs: (2,7,9) (8,12,13,14)
# Outputs:2,7,8,9,12,13,14
#---------------------------------------------------------------------------------------------#
# Case 4:
# Inputs: (empty) (2,3,4)
# Outputs: 2,3,4
#---------------------------------------------------------------------------------------------#
# Case 5: 
# Inputs: (empty) (empty)
# Outputs: empty
#---------------------------------------------------------------------------------------------#
# Case 6:
# Inputs: (2,7,9,10) (1,12,14)
# Outputs: 1,2,7,9,10,12,14
#---------------------------------------------------------------------------------------------#
# Case 7:
# Inputs: (4,7,9) (5,6,7,8)
# Outputs: 4,5,6,7,7,8,9
#---------------------------------------------------------------------------------------------#