user_input = input("Say something: ")

length = len(user_input)
print(length)
print(user_input)

# Printing each character in the string 

stringindex = 0 
while (stringindex < len(user_input)):  
    print(user_input[stringindex])
    stringindex += 1

# Given a string, if all the characters of the string are uppercase, 
# print: uppercase, lower, print: lowercase, otherwise, print: mixed case


if user_input.isupper():
    print("The string is Uppercase only")
elif user_input.islower():
    print("The string is lowercase only")
else:
    print("Mixed case")

# Print only vowels

def checkVowels():
    if (user_input[stringindex] == "a") or (user_input[stringindex] == "e") or (user_input[stringindex] == "i") or (user_input[stringindex] == "o") or (user_input[stringindex] == "u") or (user_input[stringindex] == "A") or (user_input[stringindex] == "E") or (user_input[stringindex] == "I") or (user_input[stringindex] == "O") or (user_input[stringindex] == "U"):
        print(user_input[stringindex])
stringindex = 0
print("The vowels in this string are: ")
while (stringindex < len(user_input)):  
    # check if it is a,e,i,o,u,A,E,I,O,U
    checkVowels()
    stringindex += 1

# Count the number of words in a string
# Count words in a string

# For each character in a string
    # - Check for a space, if there is a space then count as a word
    # - If there is no space, do nothing

stringindex = 0 
wordCount = 0
while (stringindex < len(user_input)):  
    if (user_input[stringindex] == ' '):
        wordCount += 1 
    stringindex += 1
if wordCount != 0:
    wordCount += 1 
print(f"Number of words in string: {wordCount}")

# Count the number of words using .split()

words = user_input.split()
print(f"Number of words in string: {len(words)}")

# Capitalize every character


