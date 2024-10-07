# Start de opdracht met onderstaande code.
deelnemers = ["Joyce", "Cederique", "Dries", "Nicky", "Thomas"]

deelnemers_talen = {    
    "Joyce": "python",    
    "Nicky": "assembly",    
    "Thomas": "ruby"
}

for deelnemer in deelnemers:
    if deelnemer in deelnemers_talen:
        print(f"Dag {deelnemer}, dankjewel voor de pol in te vullen.")
    else:
        print(f"dag {deelnemer}, gelieve de poll in te vullen.")
        poll = input("Wat is je favoriete taal: ")
        deelnemers_talen[deelnemer] = poll
print("Antwoorden op de vraag 'favoriete taal': ")
for deelnemer, taal in deelnemers_talen.items():
    print(f"- {deelnemer}: {taal}")