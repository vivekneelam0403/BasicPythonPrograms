user_input1 = input("Enter length: ")
user_input2 = input("Enter width: ")
length = int(user_input1)
width = int(user_input2)

# Input Validations
if (length < 0) | (width < 0):
    print("Pick a positive number(s)")
    exit()

perimeter = 2*length + 2*width
print (perimeter)
