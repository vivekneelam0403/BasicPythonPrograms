# Even or Odd

user_input = input("Enter a number:")
number = int(user_input)
remainder = number %2

if remainder > 0:
    print(f"{number} is a odd number")
else:
    print(f"{number} is a even number")
