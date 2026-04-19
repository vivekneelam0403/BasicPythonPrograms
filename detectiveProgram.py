# English 

# Take user input 
# set index to 0 
# loop through string while index < listlen 
    # if index and index + 1 and index + 2 == int 
        # print index, index + 1 and index + 2
# _______________________________________________________________________

'''
Testcases 

Case |       Objective      |     Input     |    Output     |
-------------------------------------------------------------
 1   | 3 digit code         | hello077hello | 077           |
-------------------------------------------------------------
 2   | No code              | hellohihey    | none          | 
-------------------------------------------------------------
 3   | 2/3 digits           | hello89fifty  | none          | 
-------------------------------------------------------------
 4   | 4/3 digits           | hello4567     | 456           |
     |                      |               | 567           | 
-------------------------------------------------------------
 5   | 2 codes; seperated   | hi670i673     | 670           | 
     |                      |               | 673           |
-------------------------------------------------------------
 6   | 2 codes; unseperated | h670673i      | 670           |
     |                      |               | 706           |
     |                      |               | 067           |
     |                      |               | 673           |
-------------------------------------------------------------
'''
# _______________________________________________________________________

# Code 


user_input = input("Enter input: ")

def detectiveProgram(user_input):
    inputLen = len(user_input) - 2
    index = 0 

    while index < inputLen:
        if (48 <= ord(user_input[index]) <= 57) and \
        (48 <= ord(user_input[index+1]) <= 57) and \
        (48 <= ord(user_input[index+2]) <= 57):
            print(f"Code found: {user_input[index],user_input[index+1],user_input[index+2]}")
        index += 1

detectiveProgram(user_input)




