# Even or Odd and positive or negitive


user_input = input("Enter a number: ")
number = int(user_input)
remainder = number %2

if (number < 0):
    print("Please pick number greater than 0")
    exit()
# If the execution comes here, it means the number is greater than 0
if (number > 0):
    print(f"{number} is positive")
  