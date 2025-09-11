# List of pairs, each pair contains the name of the student, second element contains the grade
# Print the name of all students that got A grade

# Visit each pair
#   - Check the second element of the pair, if it is "A" print the first element of the pair
#   - If it is not "A", do nothing 


pairList = [("Stdnt 1", "A"), ("Stdnt 2", "A"), ("Stdnt 3", "B"), ("Stdnt 4","C"), ("Stdnt 5", "D"), ("Stdnt 6", "F")]
print(f"{pairList}")
grades = str(input("Enter the grade: "))

listindex = 0 
print("The students that fall in this category are: ")
while (listindex < len(pairList)):
    # Check whether the element is a pair (tupe +  length check)
    # check whether the first element of pair is string
    # check whether the second element of pair is string
    if not (isinstance(pairList[listindex], tuple) and 
            len(pairList[listindex]) == 2 and 
            isinstance(pairList[listindex][0], str) and 
            isinstance(pairList[listindex][1], str)):
        continue
    if pairList[listindex][1] == grades:
        print(f"{pairList[listindex][0]}")
    listindex += 1


# Testcases 

# CASE 1: Verify the pair with the A grade, when present in the list are printed 
# Input = [("Stdnt 1", "B"), ("Stdnt 4", "A"), ("Stdnt 9", "C")]
# Output: Stdnt 4

# CASE 2: Verify that nothing is printed when there are no pairs that have a A grade
# Input = [("Stdnt 1", "B"), ("Stdnt 4", "C"), ("Stdnt 9", "D")]
# Output = None

# CASE 3: Verify that invalid is printed when a string is not typed in 
# Input = [(1, "B"), (2, "A"), (3, "C")]
# Output = Invalid

# CASE 4: Verify that nothing is printed when the input is empty
# Input = empty
# Output = None

# CASE 5:
# Input: [(Stdnt 1, "A"), (Stdnt 2, "A"), (Stdnt 3, "B"), (Stdnt 4,"C"), (Stdnt 5, "D"), (Stdnt 6, "F")]
# Outpt: Stdnt 1, Stdnt 2 