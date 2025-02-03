# Gebruik onderstaande gemengde structuur om de opdracht op te lossen.
inception_film = {
    'jaar': 2010,
    'genre': ['Actie', 'Sciencefiction', 'Thriller'],
    'cast': [ 
        {'acteur': 'Leonardo DiCaprio', 'rol': 'Cobb'},
        {'acteur': 'Joseph Gordon-Levitt', 'rol': 'Arthur'},
        {'acteur': 'Ellen Page', 'rol': 'Ariadne'}
    ],
    'locaties': ['Parijs', 'Los Angeles', 'Tokio'],
    'box_office': {'budget': 160000000, 'opbrengst': 829895144},
    'awards': {'Oscars': 0, 'Golden Globes': 4}
}
#Print de waarde van de sleutel 'cast' af, zoals aangegeven in onderstaande opdrachtprompt.
	# Tip! Spring eerst tot de sleutel 'cast'. 
    #     Gebruik dan een for-loop om over door de elementen van deze sub-dictionary te gaan.
for cast in inception_film['cast']:
    print(f"{cast['acteur']} speelt {cast['rol']}")