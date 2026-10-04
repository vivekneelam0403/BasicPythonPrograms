Robotics = {"vivek", "saket", "vishu", "achu akka", "rohan", "rahul"}
Python = {"vivek", "akhil", "atharv", "achu akka", "saket", "ayman"}

allStudents = Robotics | Python
CommonStudents = Robotics & Python
onlyRobotics = Robotics - Python
onlyPython = Python - Robotics
uniqueStudents = Robotics ^ Python

print(allStudents)
print(CommonStudents)
print(onlyRobotics)
print(onlyPython)
print(uniqueStudents)