import requests, json, os, webbrowser

search_type = input("Wil je zoeken op 'location', 'episode' of 'character id'? ").strip().lower()

if search_type == 'location':
    location_id = input("Geef een locatie id in: ")
    url_location_id = f"https://rickandmortyapi.com/api/location/{location_id}"
    response_location_id = requests.get(url_location_id)
    data_location = response_location_id.json()

    with open(r"6ICT_PROG_2024_2025\hfst_4 API\Test Folder\RickAndMorty_Data_location.json", "w") as fp:
        json.dump({'name': data_location['name']}, fp)
        fp.write("\n")
        json.dump({'type': data_location['type']}, fp)
        fp.write("\n")
        json.dump({'dimension': data_location['dimension']}, fp)
        fp.write("\n")
        json.dump({'residents': data_location['residents']}, fp)
        fp.write("\n")
        print("Data_location gedumpt!")

elif search_type == 'episode':
    episode_id = input("Geef een episode id in: ")
    url_episode_id = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response_episode_id = requests.get(url_episode_id)
    data_episode = response_episode_id.json()

    with open(r"6ICT_PROG_2024_2025\hfst_4 API\Test Folder\RickAndMorty_Data_episode.json", "w") as fp:
        json.dump({'name': data_episode['name']}, fp)
        fp.write("\n")
        json.dump({'air_date': data_episode['air_date']}, fp)
        fp.write("\n")
        json.dump({'episode': data_episode['episode']}, fp)
        fp.write("\n")
        json.dump({'characters': data_episode['characters']}, fp)
        fp.write("\n")
        print("Data_episode gedumpt!")

elif search_type == 'character':
    character_id = input("Geef een character id in: ")
    url_character_id = f"https://rickandmortyapi.com/api/character/{character_id}"
    response_character_id = requests.get(url_character_id)
    data_character = response_character_id.json()

    html_content = f"""
    <html>
    <head>
        <title>{data_character['name']}</title>
    </head>
    <body>
        <h1>{data_character['name']}</h1>
        <img src="{data_character['image']}" alt="{data_character['name']}">
        <p><strong>Status:</strong> {data_character['status']}</p>
        <p><strong>Species:</strong> {data_character['species']}</p>
        <p><strong>Type:</strong> {data_character['type']}</p>
        <p><strong>Gender:</strong> {data_character['gender']}</p>
        <p><strong>Origin:</strong> {data_character['origin']['name']}</p>
        <p><strong>Location:</strong> {data_character['location']['name']}</p>
        <p><strong>Episodes:</strong> {', '.join(data_character['episode'])}</p>
        <p><strong>URL:</strong> <a href="{data_character['url']}">{data_character['url']}</a></p>
        <p><strong>Created:</strong> {data_character['created']}</p>
    </body>
    </html>
    """

    html_file_path = os.path.join(r"6ICT_PROG_2024_2025\hfst_4 API\Test Folder", f"{data_character['name'].replace(' ', '_')}.html")
    with open(html_file_path, 'w') as html_file:
        html_file.write(html_content)

    webbrowser.open(f"file://{os.path.abspath(html_file_path)}")
    print(f"Web page for {data_character['name']} opened in browser")

else:
    print("Ongeldige keuze. Kies 'location', 'episode' of 'character'.")
