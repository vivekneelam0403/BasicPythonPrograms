# Take user input 
# set oi to 0 
# loop through list while oi < listLen
    # set ii to oi + 1 
    # loop through list while ii < listlen
        # if oivalue == iivalue 
            # print oivalue 
#_______________________________________________________________________

'''
Test cases

Case |    Input    | Output | Objective 

1    | 6,7,6,7,8,9 |  6,7   | Double duplicates

2    |  3,2,4,5,6  |  none  | No duplicates

3    |  4,4,6,5,7  |    4   | One duplicate

4    |    none     |  none  | Empty list

5    |      1      |  none  | List with one value

6    |     1,2     | none   | list with two values and no duplicates

7    |     2,2     |   2    | list with two values and one duplicate

'''
#_________________________________________________________________________

# Code 

listInput = list(map(int, input("Enter list of numbers: ").split()))

def getListDuplicates(listInput):
    oIndex = 0
    listLen = len(listInput)

    while oIndex < listLen: 
        iIndex = oIndex + 1
        while iIndex < listLen:
            if listInput[oIndex] == listInput[iIndex]:
                print(listInput[oIndex])
                break
            iIndex += 1
        oIndex += 1

print(getListDuplicates(listInput))
