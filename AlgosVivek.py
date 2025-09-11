import sys

x = int(input("Give a Number: "))

# if x is a multiple of 3 and 5, say it's a 3&5 multiple. Otherwise, say it's not.

if (x % 3 == 0) and (x % 5 == 0):
    print("Your number is a multiple of 3 & 5")
else: 
    print("Your number is not a multiple of 3 & 5")


# Given a list, if x is in the list, print the index. If not, print -1

# english??
#
# Visit each number
#     - compare it with x. If it is equal, print index. If it's not do nothing.
#     
# At the end of processing all numbers,  
# And if you found x, do nothing.
# If you didn't find, print -1

nums=[4, 5, 10, 25, 5, 15]
listindex = 0 # listindex =0
foundNumber = False
while (listindex < len(nums)): #listindex = 0 (4 < 5)
    if x == (nums[listindex]): # x=4, listindex = 0
        print (listindex) 
        foundNumber = True
    listindex += 1

if foundNumber == False:
    print("-1")

# x = 4, nums=[4, 5, 10, 25, 15]. Expected: 0, Program outout: 0 -1 -1 -1 -1
# x = 11, nums=[4, 5, 10, 25, 15]. Expected: -1,.. Program output: -1 -1 -1 -1 -1

# nums=[4, 5, 10, 25, 5, 15], x = 5.. Output?? Program output:
# 

#  4 5 10 25 15



