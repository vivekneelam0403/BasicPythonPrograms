player = {
    "Role" : "Rookie",
    "Health" : 100,
    "Level" : 1,
    "Hunger" : 0
} 


#Roles: Rookie, Warrior, Ninja, Legend

#Fight 1
print("Fight 1: ")
print("There's a fight with 5 people and player defeated 1, and player lost 40 hp and 30 hunger")
player["Health"] = 60
player["Hunger"] = 30
print(player)

#Food 
print("Found Food:")
print("player found a rabbit and cooked it and gained 15 hp and lost 30 hunger")
player["Health"] = 75
player["Hunger"] = 0
print(player)

#Fight 2
print("Fight 2:")
print("There are 23 people and player defeated 7, and player lost 160 hp in total, but found medicine, so gained back 170 hp and gained 90 hunger")
print("Level up: 4")
player["Health"] = 85
player["Hunger"] = 90
player["Level"] = 4
print(player)

#Healing
print("Found Heals:")
print("player found healing soup and gained 15 hp and lost 60 hunger")
player["Health"] = 100
player["Hunger"] = 30
print(player)

#Fight 3 
print("Fight 3:")
print("There are 15 people and player defeated 9, player lost 34 health and gained 50 hunger")
print("Level up: 18")
player["Health"] = 76
player["Hunger"] = 70 
player["Level"] = 18
print(player)

#War 
print("War declared: ")
print("Another village declared war on player's village, he healed up and found food")
player["Health"] = 100
player["Hunger"] = 0
print(player)

#Battle 1 
print("Battle 1: ")
print("There are 176 people and player defeated 6, player lost 78 hp and gained 98 hunger")
print("Level up: 21")
print("Role upgraded: Warrior")
player["Health"] = 32
player["Hunger"] = 98
player["Level"] = 21
player["Role"] = "Warrior"
print(player)

# Medicine and Food
print("Medicine and Food: ")
print("player found 3 deers and cooked them and lost 88 hunger and gained 45 health, player also gained 23 health from medicine")
player["Health"] = 100
player["Hunger"] = 10
print(player)



#Battle 2
print("Battle 2: ")
print("There are 256 people and player defeated 24, player lost 56 hp and gained 45 hunger")
print("Level up: 47")
player["Health"] = 44
player["Hunger"] = 55
player["Level"] = 47
print(player)

#Heals
print("Found Heals: ")
print("player found healing soup and maxed hp and lost all hunger")
player["Health"] = 100
player["Hunger"] = 0
print(player)

#Final Battle 
print("Final Battle:")
print("There are 587 people and player defeated 31, player lost 99 health and gained 100 hunger")
print("Level up: 78")
player["Health"] = 1
player["Hunger"] = 100
player["Level"] = 78
print(player)

#player["Armour"] = "Leather"