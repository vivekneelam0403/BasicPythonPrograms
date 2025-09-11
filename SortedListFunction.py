list1 = list(map(int, input("Enter list of numbers: ").split()))
list2 = []
threshold = int(input("Enter threshold: "))
listindex = 0 

def findMaxBelowThreshold():
    threshold = max(list1)

    while (listindex > len(list1)):
        if (list1[listindex]) < threshold:
            threshold = list1[listindex]
    listindex += 1 



