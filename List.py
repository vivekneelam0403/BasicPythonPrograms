numbers = list(map(int, input("Enter list of numbers: ").split()))

print("Printing every element:")
listindex = 0
while (listindex < len(numbers)):
    print(numbers[listindex], end=" ")
    listindex += 1

# Print every 5th element
print ("\n\nPrinting every 5th element:")
listindex = 4
while (listindex < len(numbers)): #listindex = 4 #listindex = 8
    print(numbers[listindex], end=" ") #(numbers[listindex]) = 8,6
    listindex += 5 #listindex = 4 #listindex = 9

# Print list in reverse

print("\n\nPrinting elements backwards:")
listindex = len(numbers) - 1 #listindex = 3 
while (listindex >= 0): #listindex = 3 #listindex = 2 #listindex = 1 #listindex = 0
    print(numbers[listindex], end=" ") # 6,5,4,2
    listindex -= 1 #listindex = 2 #listindex = 1 #listindex = 0

# Sample 
# 0 1 2 3 
# 2 4 5 6
# Output: 6,4


print("\n\nPrinting every alternate elements backwards:")
listindex = len(numbers) - 1
while (listindex >=0):
    print(numbers[listindex], end=" ")
    listindex -= 2

print("\n\nPrinting sum of all positive numbers:")
listindex = 0 #lisindex = 0
sumOfPositiveNumbers = 0 #listindex = 0, sumOfPositiveNumbers = 0
while (listindex < len(numbers)): #listindex = 0, sumOfPositiveNumbers = 0
    if (numbers[listindex]) > 0: #listindex = 0, sumOfPositiveNumbers = 0
        sumOfPositiveNumbers += (numbers[listindex]) #listindex = 0, sumOfPositiveNumbers = 2
    listindex += 1
print(f"{sumOfPositiveNumbers}") 
# Sample
# 0  1 2  3
# 2 -4 5 -6
# Output: 7
    