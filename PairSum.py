# Given a list of pair of numbers and a target sum, print all the pairs with the target sum 

# Taker user input of pairs 
# Take target sum 
# Visit each pair
#   - Add both numbers in the pair, if sum == targetSum then print
#   - If not do nothing 

pairList = [(2, 7), (4, 2), (8,1)]
print("Pairs are: [(2, 7), (4, 2), (8,1)]")
targetSum = int(input("Enter a sum for the pairs: "))

listindex = 0
while (listindex < len(pairList)):
    #print(f"The values before if condition are: {pairList[listindex][0]}, {pairList[listindex][1]}, f{targetSum}")
    if (pairList[listindex][0] + pairList[listindex][1]) == targetSum: 
        print(f"The pairs that have the sum are: {pairList[listindex]}")
    listindex += 1



# Testcases 

# CASE 1: Verify the pair with the target sum, when present in the list are printed 
# (2, 7), (4, 2), (8,1), (3, 5)
# Target Sum: 9
# Output: (2, 7), (8, 1)

# CASE 2: Verify that nothing is printed when there are no pairs that add up to the sum 
# (45, 67), (83, 34), (23, 45)
# Target Sum: 2
# Output: None

# CASE 3: Verify that nothing is printed when for empty list
# 'empty'
# Target Sum: 3
# Output: None

# CASE 4
# (2), (3), (4)
# Target sum: 2
# Output: Invalid