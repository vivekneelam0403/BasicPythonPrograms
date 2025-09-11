strings = list(map(str, input("Enter list of strings: ").split()))

stringindex = 0 
while (stringindex < len(strings)):
    (strings[stringindex]) = (strings[stringindex]).upper()
    stringindex += 1
print (f"The modified list: {strings}")


