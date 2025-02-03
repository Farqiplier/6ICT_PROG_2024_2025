import random


#  randint
print("Voorbeeld van randint")
getal = random.randint(1, 10) 
# 1 en 10 zijn inbegrepen (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(getal)
print("-----------------") # streepjes voor netheid


#randrange
print("Voorbeeld van randrange")
getal = random.randrange(1, 10) 
# 1 is inbegrepen, 10 is niet inbegrepen (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(getal)
print("-----------------") # streepjes voor netheid


# random
print("Voorbeeld van random")
getal2 = random.random() 
# geeft een random kommagetal tussen 0 en 1
print(getal2)
print("-----------------") # streepjes voor netheid




# Oefenmee 9
# getal1 = random.randrange(1, 6)
# getal2 = random.randrange(1, 6)
# getal3 = random.randrange(1, 6)
# print(f"{getal1} {getal2} {getal3}") # print 3 random getallen tussen 1 en 5