import requests

def get_character_info(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        character_data = response.json()
        print(f"Name: {character_data['name']}")
        print(f"Status: {character_data['status']}")
        print(f"Species: {character_data['species']}")
        print(f"Gender: {character_data['gender']}")
        print(f"Origin: {character_data['origin']['name']}")
        print(f"Location: {character_data['location']['name']}")
    else:
        print(f"Character with ID {character_id} not found.")

if __name__ == "__main__":
    character_id = input("Enter the character ID: ")
    get_character_info(character_id)