# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
spelinfo = {
    'speler1': {
        'naam': 'Alice',
        'positie': {
            'x': 10,
            'y': 5
        },
        'inventaris': {
            'wapen': 'zwaard',
            'goud': 50
        }
    },
    'speler2': {
        'naam': 'Bob',
        'positie': {
            'x': 2,
            'y': 8
        },
        'inventaris': {
            'wapen': 'boog',
            'goud': 9999999999
        }
    }
}

# Niveau 2

# print(f"De naam van speler2: {spelinfo['speler2']['naam']}")
# print(f"De positie van speler1: {spelinfo['speler1']['positie']}")
# print(f"Het wapen van speler2: {spelinfo['speler2']['inventaris']['wapen']}")

# Niveau 3

spelinfo['speler2']['inventaris']['goud'] = 0
print(spelinfo)

# Niveau 4

# spelinfo['speler1']['hacker'] = False
# spelinfo['speler2']['hacker'] = True