# Take user input for list 
# start with fIndex as 0 and bIndex as (len-1)
# loop until fIndex <= bIndex
    # fIndex == bIndex
        # print fIndex 
    # otherwise 
        # print fIndex and bIndex 
#_________________________________________________________________________________
listInput = list(map(int, input("Enter list of numbers: ").split()))

def traversingListFunction(listInput):
    

    listLength = len(listInput)

    fIndex = 0
    bIndex = listLength - 1 
    pytestResult = []

    while fIndex <= bIndex:
        if fIndex == bIndex:
            pytestResult.append(listInput[fIndex])
            print(listInput[fIndex])
        else: 
            pytestResult.append(listInput[fIndex])
            pytestResult.append(listInput[bIndex])
            print(listInput[fIndex])
            print(listInput[bIndex])
        fIndex += 1
        bIndex -= 1
    
    return pytestResult
#__________________________________________________________________________________

'''
Test Cases 

Case |    Input  |  Output

1    | 1,3,4,5,6 | 1,6,3,5,4

two  | 1,3,3,3,4 | 1,4,3,3,3

3    | 7,7,7     | 7,7,7 

4    | none      | none 

5    | 1,3,4,5   | 1,5,3,4

6    |    1      | 1 

7    | 1,3       | 1,3 
'''

