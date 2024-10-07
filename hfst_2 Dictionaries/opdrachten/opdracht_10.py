
flashkaarten = {
    "hond": "dog",
    "kat": "cat",
    "huis": "house",
    "auto": "car",
}
fouten = {}

for flashkaart, vertaling in flashkaarten.items(): 
    gevraagde = input(f"Wat is de vertaling van {flashkaart}: ")
    if gevraagde == vertaling:
        print("Dit klopt!")
    else:
        fouten[flashkaart] = vertaling
        print("Dit klopt niet!")
print("Oefen meer op deze woorden... ")
for flashkaart, vertaling in fouten.items():
    print(f"- {flashkaart}, {vertaling}")