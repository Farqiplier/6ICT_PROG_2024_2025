# Maak gebruik van onderstaande dictionary.
from curses import flash


flashkaarten = {
    "hond": "dog",
    "kat": "cat",
    "huis": "house",
    "auto": "car",
}
fouten = {}

for flashkaart, vertaling in flashkaarten: 
    input(f"Wat is de vertaling van {flashkaart}: ")
    if flashkaart == vertaling:
        print("Dit klopt!")
    else:
        fouten[flashkaart] = vertaling
        print("Dit klopt niet!")
print("Oefen meer op deze woorden... ")
for flashkaart, vertaling in fouten.items():
    print(f"- {flashkaart}, {vertaling}")