school_clubs = {
    "robotics" : ["Alex", "Maya", "Liam", "Alex"],
    "art" : ["Liam", "Sophia", "Maya"]
}

roboticsSet = set(school_clubs["robotics"])
artSet = set(school_clubs["art"])
allStudents = roboticsSet | artSet
onlyRobotics = roboticsSet - artSet





print(roboticsSet)
print(allStudents)
print(onlyRobotics)