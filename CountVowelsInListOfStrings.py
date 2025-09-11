# Print number of vowels in each string of the list 
# Sample input and output: 
#     - ["Hello", "World"] 
#     - Hello = 2 
#       World = 1

# Take user input 
# For each string in the list
#   - Check if the character is a,e,i,o,u,A,E,I,O,U then count as a vowel
#   - If not do nothing

def isVowel(character):
    if (character == "a") or (character == "e") or (character== "i") or (character == "o") or (character == "u") or (character == "A") or (character == "E") or (character == "I") or (character == "O") or (character == "U"):
        return True
    else:
        return False
def countVowels(word): # word = "Hello"
    # For each character in the word
    #    - Check whether this character is a vowel, if it is then count += 1
    #    - If not do nothing
    # return count
    countOfVowels = 0
    charindex = 0
    while (charindex < len(word)):
        # check word[charindex] is a vowel
        if (isVowel(word[charindex])):
            countOfVowels += 1
        # if (word[charindex] == "a") or (word[charindex] == "e") or (word[charindex] == "i") or (word[charindex] == "o") or (word[charindex] == "u") or (word[charindex] == "A") or (word[charindex] == "E") or (word[charindex] == "I") or (word[charindex] == "O") or (word[charindex] == "U"):
        #     countOfVowels += 1
        charindex += 1
    return countOfVowels


strings = list(map(str, input("Enter list of strings: ").split()))

stringindex = 0 
charindex = 0

while (stringindex < len(strings)):
    # Count vowels of the string
    # word = (strings[stringindex])
    # while (charIndex < len(word)):
    #     if (word[charindex] == "a") or (word[charindex] == "e") or (word[charindex] == "i") or (word[charindex] == "o") or (word[charindex] == "u") or (word[charindex] == "A") or (word[charindex] == "E") or (word[charindex] == "I") or (word[charindex] == "O") or (word[charindex] == "U"):
    #         countOfVowels += 1
    #     charIndex += 1

    # Count vowels of the string
    countOfVowels = countVowels(strings[stringindex])

    # print (count) 
    print(f"{strings[stringindex]} = {countOfVowels}")
    stringindex += 1


# For each string in the list
#   - Count vowels of the string
#   - print (count)  

# Function Design 
# Name: countVowels()
# Inputs: string
# Outputs: integer


