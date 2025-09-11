

strings = ["apple", "banana", "cherry"]

def traverseWord(word):
    print(f"Processing word: {word}")    # prints "apple"
    charIndex = 0 # stringIndex=0, word= "apple", charIndex=0
    while (charIndex < len(word)): # stringIndex=0, word= "apple", charIndex=0 
        print(f"    Processing character: {word[charIndex]}") # prints "a" prints "a" prints "a"
        charIndex += 1

stringIndex = 0
while (stringIndex < len(strings)): # stringIndex=0

    word = strings[stringIndex]  # stringIndex=0, word="apple"
    traverseWord(word)

    print("-" * 50) # Separator for clarity  
    stringIndex += 1

