Soccer = {"Vivek", "Ankush", "Hanish", "Atharv", "Aarav", "Albert", "TJ", "Nikola", "Timothy"}
Football = {"Vivek", "Akhil", "Aarav", "TJ", "Jash", "Kian", "Timothy", "Johanas", "Hanish"}

enter_name = input("Enter the name of the player: ")


if enter_name in Soccer and enter_name in Football:
    print("Soccer player and Football player")
elif enter_name in Soccer:
    print("Soccer player")
elif enter_name in Football:
    print("Football Player")
else:
    print("Not registered")






allPlayers = Soccer | Football
commonPlayers = Soccer & Football
onlySoccer = Soccer - Football
onlyFootball = Football - Soccer
uniquePlayers = Soccer ^ Football
