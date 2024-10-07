# Gebruik een zelfgemaakte dictionary (of onderstaande).
games = {
    'Terraria': 2000,
    'Minecraft': 1000,
    'Elden Ring': 400,
}
game = str(input("Voor welk spel wil je de speeltijd weten? "))
if game not in games:
    print('Je hebt dit spel niet gespeeld.')
else:
    print(f'Je hebt {games[game]} uur gespeeld.')

