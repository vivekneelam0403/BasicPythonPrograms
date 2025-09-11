# Take user input 
# 
    # Visit each number
    # If max > list[listindex], make it max 
    # append max to list2
# Print list2
# What steps am i repeating 
#  Where am i repeating 
# Visit each number in list 1 and repeat until len(list1) -1
    # Find the max below the last max 
        # Visit each number in list 1
            # If number less than last max and greater than the other numbers 
    # append to list 2 
list1 = list(map(int, input("Enter list of numbers: ").split()))
list2 = []

listindex = 0
maxOfList = max(list1) 
while (listindex < len(list1)):
    threshold = maxOfList
    maxOfList = findListMaxBelowThreshold(list1, threshold) # -1
    list2.append(maxOfList) # list2 = [21, 7, 4, 0, -1]
    listindex += 1

print (f"The sorted list is: {list2}")

#    maxNumber = (list1[0])
#    x = 1
#    while x < len(list1):
#        if ((list1[x]) < maxNumber):
#            maxNumber = list1[x]
#        x += 1


# Testcases 

# CASE 1: Verify the list gets sorted 
# Input: 1 2 9 5
# Output: 9 5 2 1

# CASE 2: empty 
# Input: empty
# Output: empty 

