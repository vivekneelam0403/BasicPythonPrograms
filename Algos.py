import sys

x = int(input("Give a Number: "))

# Type cast string to integer


# if numbxer is > 5, say it;'s greater, otherwise say it's lower

if x > 5:
    print("Your number is greater than 5")
else:
    print("Your number is lower than 5")

# if x is a multiple of 3, say it's a 3 multiple. Otherwise, say it's not.

y = x%3

if y == 0:
    print("Your number is a multiple of 3")
else:
    print("Your number isn't a multiple of 3")


# if x is a multiple of 3 and 5, say it's a 3&5 multiple. Otherwise, say it's not.

if (x % 3 == 0) and (x % 5 == 0):
    print("Your number is a multiple of 3 & 5")
else: 
    print("Your number is not a multiple of 3 & 5")


# print numbers from 0 to x
int(n) = x

for i in range(0,n):
    print(n)
    n = n - 1
    if n == 0:
        print("0")
        sys.exit("Exiting due to a condition that ''n'' is now entering negative intergers.")


# print sum of numbers from 0 to x.

int(y) = x
a = []
for i in range(0,y):
    print(y)
    b = y
    y = y - 1
    a.append(y)
    z = y + b
    
# Given a list, if x is in the list, print the index. If not, print -1

# english??
#
# Visit each number
#     - compare it with x. If it is equal, print index. If it's not do nothing.
#     
# At the end of processing all numbers, compare what you fiund with others. 
# And if you found x, do nothing.
# If you didn't find, print -1

nums=[4, 5, 10, 25, 15]
listindex = 0 # listindex =0
foundNumber = False
while (listindex < len(nums)): #listindex = 0 (4 < 5)
    if x == (nums[listindex]): # x=4, listindex = 0
        print (listindex) 
        foundNumber = True
    listindex += 1

foundNumber

# x = 4, nums=[4, 5, 10, 25, 15]. Expected: 0, Program outout: 0 -1 -1 -1 -1
# x = 11, nums=[4, 5, 10, 25, 15]. Expected: -1,.. Program output: -1 -1 -1 -1 -1

# nums=[4, 5, 10, 25, 5, 15], x = 5.. Output?? Program output:
# 

#  4 5 10 25 15


# 0 1 2 3
# Maintain a running sum
# Visit each number
#     - add that number to my running sum
# print that running sum

runningSum = 0
for i in range(0,x): # 0 1 2 3 
    runningSum = runningSum + i
print "runningSum"


