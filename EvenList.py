# Take user input
# Turn user input into a list
# Divide each number by 2
# Check for remainder
# Print the number of even numbers

# Sample: 12, 13, 14, 25

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# remainder = numbers % 2
# count = 0

# while True:
#     if remainder == 0: 
#         count += 1
   
# Divide each number by 2
# Converting this to prgramming steps
#     - Identifying that there was a repitition of steps at each number.. so, loop is involved <=== NO
#     - Designing a basic loop that visits every number <==
#     - After this, add the steps that  need to be done at each number
#         - check whether the number is even. If so, increment your counter

# Designing a basic loop that visits every number
# 

listindex = 0 
while (listindex < len(numbers)):  
    print(numbers[listindex])
    listindex += 1
    


