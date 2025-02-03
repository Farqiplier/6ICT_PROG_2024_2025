""" TOETS Hoofdstuk 2 -- Gebruik & Doorlopen van Dictionaries (  / 10)
De dictionary 'aandelen' stelt de aandelenportefeuille van een persoon voor.
    - Niveau 1: maak een overzicht van de aandelen.
    - Niveau 2: zorg dat de persoon aandelen kan (ver)kopen.

Het is niet verplicht om commentaar bij te code te schrijven.
Je kan dit wel doen als je de code wat meer wilt toelichten.
"""

aandelen = {
    "S&P 500": 10,
    "IWDA": 2,
}

""" Niveau 1 (   / 2)
Print een overzicht van de aandelen in de dictionary.
Zie het voorbeeld hieronder voor de opbouw van de print.
De code moet blijven werken, ook als de dictionary erna wijzigt.

VOORBEELD
---------
Uw aandelenportefeuille ziet er als volgt uit.
    - 10 shares in S&P 500.
    - 2 shares in IWDA.

"""
# print("Uw aandelenportefeuille ziet er als volgt uit.")
# for aandeel, shares in aandelen.items():
#     print(f"    - {shares} shares in {aandeel}.")


""" Niveau 2 (  / 8)
Herhaal het volgende tot in het oneindige.

    Vraag de gebruiker naar een aandeel.
    Vraag de gebruiker naar hoeveel shares van het aandeel deze wilt (ver)kopen.
    Wijzig de dictionary 'aandelen' om aan het verzoek van de gebruiker te voldoen.
    Print hoeveel shares van dit aandeel er nu in de dictionary zitten (zie voorbeeld).

Het herhalen moet stoppen wanneer de gebruiker 'STOP' invult in plaats van een aandeel.
Print tenslotte de gewijzigde dictionary (gebruik evt. de code uit niveau 1).

Hou rekening met volgende zaken.
    - Het aandeel bestaat al in de dictionary? Wijzig het element dan.
    - Het aandeel bestaat niet in de dictionary? Voeg dan een nieuw element toe.
    - In beide gevallen mag er nooit een negatief aantal shares in de dictionary staan.
      Mocht dit het geval zijn, print dan een fout in plaats van de dictionary te wijzigen.

VOORBEELD
---------
>>> Selecteer een aandeel: S&P 500
>>> Hoeveel shares (ver)kopen: -5
Het aandeel 'S&P 500' is gewijzigd. U heeft nu 5 shares in dit aandeel.

>>> Selecteer een aandeel: IWDA
>>> Hoeveel shares (ver)kopen: -5
Fout! U beschikt slechts over 2 shares in 'IWDA'. 5 verkopen is niet mogelijk.

>>> Selecteer een aandeel: EMIM
>>> Hoeveel shares (ver)kopen: 3
Het aandeel 'EMIM' is gewijzigd. U heeft nu 3 shares in dit aandeel.

>>> Selecteer een aandeel: STOP
Uw aandelenportefeuille ziet er als volgt uit.
    - 5 shares in S&P 500.
    - 2 shares in IWDA.
    - 3 shares in S&P 500.

"""
aandeel_gebruiker = ""
while True:
    aandeel_gebruiker = input(">>> Selecteer een aandeel: ")
    shares_gebruiker = int(input(">>> Hoeveel shares (ver)kopen: "))
    if aandeel_gebruiker in aandelen:
        if (aandelen[aandeel_gebruiker] + shares_gebruiker) < 0:
            shares_gebruiker *= -1
            print(f"Fout! U beschikt slechts over {aandelen[aandeel_gebruiker]} shares in '{aandeel_gebruiker}'. {shares_gebruiker} verkopen is niet mogelijk.")
            
        else:
            aandelen[aandeel_gebruiker] += shares_gebruiker
            print(f"Het aandeel {aandeel_gebruiker} is gewijzigd. U heeft nu {aandelen[aandeel_gebruiker]} shares in dit aandeel.")
    else:
        aandelen[aandeel_gebruiker] = 0
        if (aandelen[aandeel_gebruiker] + shares_gebruiker) < 0:
            shares_gebruiker *= -1
            print(f"Fout! U beschikt over GEEN shares in '{aandeel_gebruiker}'. {shares_gebruiker} verkopen is niet mogelijk.")
        else:
            aandelen[aandeel_gebruiker] = shares_gebruiker
            print(f"Het aandeel {aandeel_gebruiker} is gewijzigd. U heeft nu {aandelen[aandeel_gebruiker]} shares in dit aandel.")
for aandeel, shares in aandelen.items():
    print(f' - {shares} shares in {aandeel}.')







