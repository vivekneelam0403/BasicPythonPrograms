# Take user input for string 
# Take user input for character 
    # loop through string while index < string length 
        # if string == character 
            # add 1 to count 
# print count 
#___________________________________________________________________

'''
Test cases 

Case |   Input    | Output 

1    | banana; a  |    3

2    |   hi; i    |    1

3    | alfredo; n |    0 

4    | none; none |    0 

5    |   none; a  |    0

'''
#____________________________________________________________________

# Code 

string_input = str(input("Enter string: "))
char_input = str(input("Enter characeter: "))

def characterCountFunction(string_input, char_input):
    stringLength = len(string_input)
    index = 0 
    count = 0 

    while index < stringLength: 
        if string_input[index] == char_input: 
            count += 1 
        index += 1 
    return count