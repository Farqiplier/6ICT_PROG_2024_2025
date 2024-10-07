# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
while True:
    for fruit, aantal in fruitmand.items():
        bijkopen = input(f"Hoeveel {fruit} aankopen (huidig aantal: {aantal}): ")
        fruitmand[fruit] += bijkopen
    if bijkopen == "nee":
            break


print("In de fruitmand zit momenteel.")
for fruit, aantal in fruitmand.items():
    print(f"- {aantal} {fruit}")