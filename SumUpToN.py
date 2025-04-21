
# Psudo Code
# Get input from user
#
# Validate input
#
# Initialize "SumSofar" to 0
# for each number up to N
#    Add this number to "SumSoFar"
#
# print "SumSofar"

user_input = input("Enter a number: ")
number = int(user_input)  # number is 5

# Inut Validations
if (number < 0):
    print ("Pick a positive number")
    exit()

# Calculate the sum
sumSoFar = 0  
for num in range(number+1): # Generates numbers from 0 to 4. number os set to 0
    sumSoFar = num + sumSoFar

# Print the sum
print (f"The sum of 0 to {number} is {sumSoFar}")

#Testcases
# 1. 5
# 2. -1
# 3. 0
# Advanced
# 4. Very very very big number
