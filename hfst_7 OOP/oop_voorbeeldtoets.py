""" PUNTENVERDELING 
    - (1) Klasse aanmaken met hoofdletter.
    - (2) Klasse bevat zinvolle eigenschappen (ondergrens, bovengrens, temperatuur, opt. status)
    - (5) Klasse bevat correcte methoden (start, stop, reset, tijd, init)
        * (1) init: initieert alle nodige eigenschappen op correcte wijze.
        * (2) meten: meet een willekeurige temperatuur tussen 0°C en 50°C
                     & geeft waarschuwing als temperatuur buiten de grenzen is.
        * (1) controleren: controleert of de temperatuur oke, te koud of te warm is.
        * (1) kalibreren: stel een nieuwe ondergrens en bovengrens in.
    - (1) Code is gestructureerd opgebouwd met duidelijke namen.
    - (1) Object van klasse aangemaakt en getest.
"""

""" THERMOMETER UITLEG (   / 10)
Je krijgt hieronder een korte beschrijving van een temperatuursensor.
Maak op basis van deze beschrijving een klasse met correcte eigenschappen en methoden.
Maak ook een object aan van deze klasse waarin je alle onderdelen van de sensor test.

Bij het aanmaken van de sensor geef je een ondergrens en bovengrens voor de temperatuur mee.
De temperatuursensor moet volgende zaken kunnen:
    - Meet een temperatuur (simuleer dit door een willekeurige waarde te genereren tussen 0°C en 50°C).
    - Een waarschuwingsmelding tonen als de temperatuur buiten de grenzen valt.
    - De huidige temperatuur en status van de sensor controleren (oke, koud of warm).
    - Het herkalibereren van de ondergrens en bovengrens.
    
Belangrijk! Bij elke actie moet duidelijk aangegeven worden wat er gebeurt.
"""


""" THERMOMETER VOORBEELD (ondergrens 10°C en bovengrens 30°C)
De gebruiker meet een temperatuur, het is nu 25°C

De gebruiker controleert de huidige temperatuur.
De temperatuur van 25°C is oke.

De gebruiker meet een temperatuur, het is nu 8°C.
WAARSHUWING! Temperatuur ligt buiten de grens

De gebruiker controleert de huidige temperatuur.
De temperatuur van 8°C is te koud.

De gebruiker stelt nieuw grenzen in: 5°C en 40°C

De gebruiker controleert de huidige temperatuur.
De temperatuur van 8°C is oke.

De gebruiker meet een temperatuur, het is nu 44°C
WAARSHUWING! Temperatuur ligt buiten de grens

De gebruiker controleert de huidige temperatuur.
De temperatuur van 44°C is te warm.
"""
import random

class Thermometer:
    def __init__(self, ondergrens:int, bovengrens:int) -> None:
        self.ondergrens = ondergrens
        self.bovengrens = bovengrens
        self.temperatuur = 0
        self.status = ""

    def meten(self) -> None:
        self.temperatuur = random.randint(0, 50)
        print(f"De gebruiker meet een temperatuur, het is nu {self.temperatuur}°C")
        if (self.temperatuur > self.bovengrens) or (self.temperatuur < self.ondergrens):
            print("WAARSHUWING! Temperatuur ligt buiten de grens") 
    
    def controleren(self) -> None:
        if self.temperatuur < self.ondergrens:
            self.status = "te koud"
        elif self.temperatuur > self.bovengrens:
            self.status = "te warm"
        else:
            self.status = "oke"
        print(f"De temperatuur van {self.temperatuur}°C is {self.status}.")

    def kalibreren(self, nieuwe_ondergrens:int , nieuwe_bovengrens:int ) -> None:
        self.ondergrens = nieuwe_ondergrens
        self.bovengrens = nieuwe_bovengrens
        print(f"De gebruiker stelt nieuwe grenzen in: {self.ondergrens}°C en {self.bovengrens}°C")

therm = Thermometer(0, 30)
therm.meten()
therm.controleren()
therm.kalibreren(10, 20)
therm.controleren()
therm.meten()
therm.controleren()