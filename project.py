import requests

while True:
    user_input = input("What pokemon will you choose? ")
    user_input = user_input.lower()

    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_input}")
    if req.status_code == 200:
        pokemon = req.json()
        print(f"Name is: {pokemon['name']}")
        print("Abilites: ")
        for ability in pokemon['abilities']:
            print(ability['ability']['name'])
    else: 
        print("Pokemon not found. Try again!")