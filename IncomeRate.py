# Take user input (annual expense)
# Set income tax rate to 20%
# Divide annual expense by 0.80 (totalSum)
# Subtract annual expense from totalSum
# Print sum (Income)


# Sample test case: 1000 monthly expense
# 1000/0.20 = 5000
# 5000 - 1000
# Print 4000
# Why expense? How much I need to each to be able to get enough to cover 
# my expenses and pay taxes !!
# Income (I)
# Pay taxes = 20% * I
# Reamining = I - 20% * I = 80% * I
# E = 80% * I
# I = E/80%

user_input = input("Enter your annual expense: ")
annualExpenses = int(user_input)

annualIncome = annualExpenses/0.80
print (f"Your annual income should be ${annualIncome}")
