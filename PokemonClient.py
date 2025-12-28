import requests 

pokemon = input("Enter a Pokemon name: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
response = requests.get(url)

if response.status_code == 200: 
    data = response.json()
    print("Name:", data["name"])
    print("Height:", data["height"])
    print("Weight:", data["weight"])
    print("\nAbilities:")
    for ability in data["abilities"]:
        print("-", ability["ability"]["name"])
else:
    print("Pokemon not found!")