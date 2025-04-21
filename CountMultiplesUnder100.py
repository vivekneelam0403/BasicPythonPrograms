#Psudo Code
# Get input from user
#
# Validate input
#
# Divide "number" by 10
# print "Multiple counter"


user_input = input("Enter a number: ") # user gave 3
number = int(user_input) # number contains 2

# Input Validations
if (number <= 0): # the if statement evaluates to false
    print ("Pick a positive number")
    exit()

multiple = int(100/number) # number divided by 10 and multipled contains 5 

print (f"{multiple}") 

#Test Cases:
# 1.2 answer: 5
# 2.-1 answer: invalid
# 3. 0 answer: invalid
