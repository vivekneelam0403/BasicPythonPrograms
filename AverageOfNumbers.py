# Take the user input (the numbers)
# Find the sum of the numbers given by user
# Divide the sum by the amount of numbers
# Print the average

total = 0
count = 0

while True: 
    user_input1 = input("Enter a number (type done when finished): ")
    if user_input1 == "done":
        break

    total += float(user_input1)
    count += 1

if count > 0: 
    average = total/count
    print (f"The average is {average}")
