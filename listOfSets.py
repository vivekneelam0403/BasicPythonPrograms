listOfSets = [{"akhil", "atharv", "vivek", "bharath"}, {"atharv", "vivek", "bharath"}, {"akhil", "atharv", "vivek", "bharath", "saket"}]

top10List = ["vivek", "akhil", "saket", "atharv", "akshita", "ayman", "bharath", "ankush", "jacob", "micheal"]

print(top10List[0])
print(top10List[1])
print(top10List[2])

daily_students = listOfSets[0] & listOfSets[1] & listOfSets[2]

print(daily_students)

total_attendance = 0 

for day in listOfSets:
    total_attendance += len(day)

print(total_attendance)


print(a)