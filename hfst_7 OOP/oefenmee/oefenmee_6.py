# Werk verder met de klasse Hond van oefen mee 4.
class Hond:
    massa = 10
    naam = "Lassie"

    def __init__(self, naam:str, massa:int) -> None:
        self.naam = naam
        self.massa = massa

    def blaf(self) -> None:
        print(f"{self.naam} zegt blaf" )

    def weegschaal(self) -> None:
        print(f"{self.naam} weegt {self.massa} kg")    

    def wijzig_naam(self, naam: str) -> None:
        print(f"{self.naam} heet nu {naam}")
        self.naam = naam

hond = Hond()
hond_2 = Hond()
hond = Hond("Fifi", 3)

" Via onderstaande code kan je niveau 2 testen. "
# hond_1.weegschaal()
# hond_2.weegschaal()
