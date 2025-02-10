import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '71865e24de0f30c63b0aee7bfc5f750b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_name_change = {
    "pokemon_id": "230131",
    "name": "New-Name",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "230131"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_name_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name_change)
print(response_name_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)