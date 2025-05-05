# Werk verder met de klasse Hond van oefen mee 2.
class Hond:
    massa = 10
    naam = "Lassie"

    def benoem(self, naam: str) -> None:
        self.naam = naam

    def blaf(self) -> None:
        print(f"{self.naam} zegt blaf" )

    def weegschaal(self) -> None:
        print(f"{self.naam} weegt {self.massa} kg")
    
    def wegen(self, massa:int) -> None:
        self.massa = massa

    

" Via onderstaande code kan je niveau 1 testen. "
# hond = Hond()
# hond.benoem("Fleur")
# print( hond.naam )
# hond.blaf()

" Via onderstaande code kan je niveau 2 testen. "
dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
print( dier.massa )
dier.weegschaal()

# hond.weegschaal() 