# Maak Conway's Game of Life na. https://www.youtube.com/watch?v=C2vgICfQawE

""" OPGELET!
ONDERAAN DIT DOCUMENT STAAN 2 REGELS IN COMMENTAAR.
HAAL DEZE UIT COMMENTAAR ALS JE HET SPEL WILT STARTEN IN PYGAME.

DOE DIT PAS ALS JE DE FUNCTIE regels_game_of_life HEBT VOLTOOID.

"""

""" --------------- Benodigde modules --------------- """  
import copy
import random
import pygame

""" --------------- Globale variabelen (lees zeker na!) --------------- """
# De grootte van het bord, in aantal cellen.
# Het staat je vrij om deze aan te passen (het moeten wel gehele getallen zijn).
#
# Met BREEDTE = 3 en HOOGTE = 4, kan een speelbord
# er als volgt uit zien.
# [
#    [0,0,1],
#    [0,1,1],
#    [0,0,1],
#    [1,0,0]
# ]
HOOGTE = 100
BREEDTE = 100

# De breedte en hoogte van iedere cel in pixels.
# Het staat je vrij om deze aan te passen (het moeten wel gehele getallen zijn).
# LET OP! Zet deze niet te groot, anders zal het Pygame venster groter worden dan het scherm.
CEL_HOOGTE = 5
CEL_BREEDTE = 5

# De kans die een dode cel heeft om levend te worden in het begin.
# Het staat je vrij om deze aan te passen (waarde tussen 0-1).
KANS_LEVEND = 0.1

""" --------------- Te ontwikkelen functies !! VOEG ZELF TYPEHINTS TOE !! --------------- """
def maak_dood_bord(hoogte, breedte):
    bord = []
    for _ in range(hoogte):
        rij = []
        for _ in range(breedte):
            rij.append(0)
        bord.append(rij)
    return bord
    """ return een 2D-lijst gevuld met nullen (dode cellen)

        hoogte: het aantal lijsten in de geneste lijst.
        breedte: het aantal nullen in iedere lijst.

        Tip! Zoek online op hoe je dit doet.
    """
    return None


# print( maak_dood_bord(2,2) ) # Zie uitkomst in bovenstaande string.
"""
[ 
  [0, 0],
  [0, 0]
]
"""
# print( maak_dood_bord(3,4) ) # Zie uitkomst in bovenstaande string.
"""
[ 
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
]
"""

########################################


def bord_start_staat(bord, kans_levend):
    bord = []
    
    """ return een bord, waarbij willekeurige cellen een waarde 1 bevatten 
    
        bord: het bord bekomen uit maak_dood_bord (dus volledig gevuld met nullen).
        kans_levend: de kans (tussen 0 en 1) die een cel heeft om waarde 1 te krijgen.

        Overloop alle cellen in de geneste lijst. Een aantal van deze cellen moet 
        waarde 1 krijgen. Om te bepalen welke gebruik je kans_levend en de random module.
    """
    return None

# bord = [
#         [0, 0, 0],
#         [0, 0, 0]
# ]
# print( bord_start_staat(bord, 0.5) ) # Verander 1 naar 0 & 0.5  # Zie uitkomst in onderstaande string.
""" kans_levend = 1     # kans_levend = 0       # kans_levend = 0.5 (is iedere keer anders)
[                       # [                     # [
    [1, 1, 1],          #    [0, 0, 0],         #   [1, 1, 0],  
    [1, 1, 1]           #    [0, 0, 0]          #   [1, 0, 1],  
]                       # ]                     # ]
"""


########################################


def get_buur_links(bord, y, x):
    """ return de waarde van de cel links van de huidige cel 
   
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
        Als de huidige cel zich op de linkergrens bevindt, return 0.
            Tip! Welke index hebben alle cellen op de linkergrens gemeenschappelijk?
    """
    return None

# bord = [
#     [1, 2],
#     [3, 4]
# ]
# print( get_buur_links(bord, 1, 1) ) # 3 (huidige cel is 4) 
# print( get_buur_links(bord, 0, 1) ) # 1 (huidige cel is 2)
# print( get_buur_links(bord, 1, 0) ) # 0 (huidige cel is 3)


########################################


def get_buur_rechts(bord, y, x):
    """ return de waarde van de cel rechts van de huidige cel 
   
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
        Als de huidige cel zich op de rechtergrens bevindt, return 0.
            Tip! Gebruik hiervoor de lengte van een rij van het bord.
    """
    return None

# bord = [
#     [1, 2],
#     [3, 4]
# ]
# print( get_buur_rechts(bord, 0, 0) ) # 2 (huidige cel is 1)
# print( get_buur_rechts(bord, 0, 1) ) # 0 (huidige cel is 2)
# print( get_buur_rechts(bord, 1, 0) ) # 4 (huidige cel is 3)


########################################


def get_buur_boven(bord, y, x):
    """ return de waarde van de cel boven de huidige cel 
        
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
        Als de huidige cel zich op de bovengrens bevindt, return 0.
    """
    return None

# bord = [
#     [1, 2],
#     [3, 4]
# ]
# print( get_buur_boven(bord, 1, 1) ) # 2 (huidige cel is 4)
# print( get_buur_boven(bord, 0, 1) ) # 0 (huidige cel is 2)
# print( get_buur_boven(bord, 1, 0) ) # 1 (huidige cel is 3)


########################################


def get_buur_onder(bord, y, x):
    """ return de waarde van de cel onder de huidige cel 
   
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
        Als de huidige cel zich op de ondergrens bevindt, return 0.
    """
    return None

# bord = [
#     [1, 2],
#     [3, 4]
# ]
# print( get_buur_onder(bord, 1, 1) ) # 0 (huidige cel is 4)
# print( get_buur_onder(bord, 0, 1) ) # 4 (huidige cel is 2)
# print( get_buur_onder(bord, 0, 0) ) # 3 (huidige cel is 1)


########################################


def get_buur_linksboven(bord, y, x):
    """ return de waarde van de cel linksboven de huidige cel 
   
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
        Als de huidige cel zich op de linkergrens bevindt, return 0.
        Als de huidige cel zich op de bovengrens bevindt, return 0.
            Tip! Combineer de oplossingen van get_buur_links & get_buur_boven.

    """
    return None

# bord = [
#     [1, 2],
#     [3, 4]
# ]
# print( get_buur_linksboven(bord, 1, 1) ) # 1 (huidige cel is 4)
# print( get_buur_linksboven(bord, 0, 1) ) # 0 (huidige cel is 2)
# print( get_buur_linksboven(bord, 1, 0) ) # 0 (huidige cel is 3)


########################################


def get_buur_rechtsboven(bord, y, x):
    """ return de waarde van de cel rechtsboven de huidige cel 
   
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
        Als de huidige cel zich op de rechtergrens bevindt, return 0.
        Als de huidige cel zich op de bovengrens bevindt, return 0.
    """
    return None

# bord = [
#     [1, 2],
#     [3, 4]
# ]
# print( get_buur_rechtsboven(bord, 1, 1) ) # 0 (huidige cel is 4)
# print( get_buur_rechtsboven(bord, 0, 1) ) # 0 (huidige cel is 2)
# print( get_buur_rechtsboven(bord, 1, 0) ) # 2 (huidige cel is 3)


########################################


def get_buur_linksonder(bord, y, x):
    """ return de waarde van de cel linksonder de huidige cel 
   
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
        Als de huidige cel zich op de linkergrens bevindt, return 0.
        Als de huidige cel zich op de ondergrens bevindt, return 0.
    """
    return None

# bord = [
#     [1, 2],
#     [3, 4]
# ]
# print( get_buur_linksonder(bord, 1, 1) ) # 0 (huidige cel is 4)
# print( get_buur_linksonder(bord, 0, 1) ) # 3 (huidige cel is 2)
# print( get_buur_linksonder(bord, 1, 0) ) # 0 (huidige cel is 3)


########################################


def get_buur_rechtsonder(bord, y, x):
    """ return de waarde van de cel rechtsonder de huidige cel 
   
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
        Als de huidige cel zich op de rechtergrens bevindt, return 0.
        Als de huidige cel zich op de ondergrens bevindt, return 0.
    """
    return None

# bord = [
#     [1, 2],
#     [3, 4]
# ]
# print( get_buur_rechtsonder(bord, 1, 1) ) # 0 (huidige cel is 4)
# print( get_buur_rechtsonder(bord, 0, 1) ) # 0 (huidige cel is 2)
# print( get_buur_rechtsonder(bord, 0, 0) ) # 4 (huidige cel is 1)


########################################


def tel_levende_buren(bord, y, x):
    """ return het aantal naburige cellen dat leeft

        bord: het bord met cellen.
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
    
        Naburige cellen bevinden zich in de 8 indexen rondom de huidige cel.
        Cellen met een waarde 1 zijn levend, cellen met een waarde 0 zijn dood.
            Tip! In de get-functies haalde je de waarde op van de cellen. Je weet dat deze waarde 1 of 0 is.
                 Maak een teller aan en gebruik deze in combinatie met de get_functies.
    """
    return None

# bord = [
#     [1, 1, 0],
#     [0, 1, 0],
#     [1, 0, 0]
# ]
# print( tel_levende_buren(bord, 1, 0) ) # 4
# print( tel_levende_buren(bord, 2, 1) ) # 2
# print( tel_levende_buren(bord, 0, 0) ) # 2
# print( tel_levende_buren(bord, 2, 0) ) # 1


########################################


def regels_game_of_life(bord, y, x):
    """ return True als de huidige cel zal (blijven) leven, False als het dood gaat/blijft. 

        bord: het bord met cellen.
        y: de y-index van de huidige cel.
        x: de x-index van de huidige cel.
        
    
        De return-waarde MOET een boolean zijn. Baseer je op de regels van Game of Life.
    """
    return None

# bord = [          # bord_volgend_frame = [
#     [1, 1, 0],    #     [1, 1, 0],                                                
#     [0, 1, 0],    #     [0, 1, 0],                                               
#     [1, 0, 0]     #     [0, 0, 0], 
# ]                 # ]
# print( regels_game_of_life(bord, 0, 0) ) # True
# print( regels_game_of_life(bord, 0, 1) ) # True
# print( regels_game_of_life(bord, 0, 2) ) # False
# print( regels_game_of_life(bord, 1, 0) ) # False
# print( regels_game_of_life(bord, 1, 1) ) # True
# print( regels_game_of_life(bord, 1, 2) ) # False
# print( regels_game_of_life(bord, 2, 0) ) # False
# print( regels_game_of_life(bord, 2, 1) ) # False
# print( regels_game_of_life(bord, 2, 2) ) # False


########################################


# Deze functie is reeds gemaakt. Overloop hem wel. Snap je wat er gebeurt?
# Zo nee, vraag om extra uitleg.
def update_bord(bord):
    """ Update het bord volgens de regels van Game of Life """
    # Maak een kopie van het huidige bord
    huidig_bord = copy.deepcopy(bord)

    # Bepaal welke cel leeft/sterft. Update het bord op basis hiervan.s
    for y, rij in enumerate(huidig_bord):
        for x, _ in enumerate(rij):
            leeft = regels_game_of_life(huidig_bord, y, x)
            if leeft:
                bord[y][x] = 1
            else:
                bord[y][x] = 0

""" --------------- game-loop --------------- """
def main():
    pygame.init()
    screen = pygame.display.set_mode((BREEDTE * CEL_HOOGTE, HOOGTE * CEL_HOOGTE))
    clock = pygame.time.Clock()

    bord = maak_dood_bord(HOOGTE, BREEDTE)
    bord_start_staat(bord, KANS_LEVEND)

    running = True
    while running:
        # Maak scherm wit. Update vervolgens OBV cel-waarde.
        screen.fill((250, 250, 0))
        for y, rij in enumerate(bord):
            for x, cel in enumerate(rij):
                if cel:
                    color = (255, 0, 0)
                else:
                    color = (0, 255, 0)
                # Kleur viekant op scherm OBV kleur cel.
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        x * CEL_BREEDTE,
                        y * CEL_HOOGTE,
                        CEL_BREEDTE,
                        CEL_HOOGTE,
                    ),
                )

        # Update all cellen in het bord.
        update_bord(bord)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)


# if __name__ == "__main__":
#     main()