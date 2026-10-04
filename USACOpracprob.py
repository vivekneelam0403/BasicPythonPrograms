startInput = int(input("Start: "))
endInput = int(input("End: "))
Tele1 = int(input("Teleporter 1: "))
Tele2 = int(input("Teleporter 2: "))	

steps = abs(endInput - startInput)
path1 = abs(startInput - Tele1) + abs(endInput - Tele2)
path2 = abs(startInput - Tele1) + abs(endInput - Tele2)


if(steps >= path1) and (steps >= path2):
    print(steps)
elif (path1 >= steps) and (path1 >= path2):
    print(path1)
else:
    print(path2)