# Take user input 
# Check each number for a sign
# If there is no sign, return "-"
    # If there is a minus sign return "+"
# Print 

# Take user input (which is a list)
# For each number in the list
#     - Multiply by -1
#     - Print the resulting number
# 


numbers = list(map(int, input("Enter list of numbers: ").split()))

listindex = 0 
while (listindex < len(numbers)):  
    (numbers[listindex]) = (numbers[listindex]) * -1   
    listindex += 1
print(f"The Modified List: {numbers}")


# User give a number
# Multiple by -1 and print it
