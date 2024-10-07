# Start de oefen mee met onderstaande dictionary.
talen =    ["Python", "Java", "Javascript", "C#", "PHP", "Overig"]
aandelen = [29.48   , 17.18 , 9.14        , 6.94, 6.49 , 9.93]

taal_aandeel = {} # Zet lege dict klaar.
for index, taal in enumerate(talen): # Overloop een van de lijsten.
    taal_aandeel[taal] = aandelen[index] # Voeg de waarde toe aan de dict.
    pass
print(taal_aandeel) # Print de dict.