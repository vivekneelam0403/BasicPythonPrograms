# Day of the week. Write a python program, that takes a number between 1 and 7, and prints the day
#  of the week. 1 = Monday, 2= Tuesday, and so on.

day = int(input("Enter a number: "))
day = input("Enter a number: ")

# Input Validations
if (day > 7) | (day < 1):
    print ("Please enter a number between 1-7")
    exit()

# Sunday = 1
# Monday = 2
# Tuesday = 3
# Wednesday = 4
# Thursday = 5
# Friday = 6
# Saturday = 7

# If user gives 1, then output is Sunday 

if (day == 1):
    print("Sunday")
elif (day == 2):
    print("Monday")
elif (day == 3):
    print("Tuesday")
elif (day == 4):
    print("Wednesday")
elif (day == 5):
    print("Thursday")
elif (day == 6):
    print("Friday")
else:
    print("Saturday")
