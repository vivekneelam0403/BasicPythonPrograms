numbers = list(map(int, input("Enter list of numbers: ").split()))
# list = [20, 42, 5, 7, 6, -1]
# Excpected Output: 20, -1, 42, 6, 5 ,7
# list = [20, 42, 5, 6, -1]

forwardIndex = 0 
backwardIndex = len(numbers) - 1
while (forwardIndex <= backwardIndex): 
    if (forwardIndex == backwardIndex):
        print(numbers[backwardIndex])
    else:
        print(numbers[forwardIndex]) 
        print(numbers[backwardIndex]) 
    forwardIndex += 1 #forwardIndex = 2, backwardIndex = 3
    backwardIndex -= 1 #forwardIndex = 2, backwardIndex = 2
