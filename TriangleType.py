# Given 3 sides of a triangle return one if it is equilateral, return 2 if it is isocles, otherwise 3 

user_input1 = input("Enter a Side1: ")
user_input2 = input("Enter a Side2: ")
user_input3 = input("Enter a Side3: ")
side1 = int(user_input1) # Type cast string to integer
side2 = int(user_input2) # Type cast string to integer
side3 = int(user_input3) # Type cast string to integer
if (side1 == side2) & (side1 == side3):
    print("1")
elif (side1 == side2) | (side2 == side3) | (side3 == side1):
    print("2")
else:
    print("3")
  
