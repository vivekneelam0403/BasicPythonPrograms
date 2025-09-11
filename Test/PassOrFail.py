user_input = input("Enter the grade: ")
number = int(user_input)

# Input validations
if (number > 100) | (number < 0):
    print("Please enter a number from the range of 0-100")
    exit()

if (number >= 60):
    print("Pass")
else:
    print("Fail")
