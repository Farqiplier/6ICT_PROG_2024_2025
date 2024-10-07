# Vul onderstaande dictionary aan met behulp van input.
relaties = {}
while True:
    relatie = str(input("Geef relatie tot persoon op: "))
    if relatie == "stop":
        break
    naam = str(input("Geef naam van persoon op: "))
    if naam == "stop":
        break
    relaties[relatie] = naam
    print('----------------')
print(relaties)