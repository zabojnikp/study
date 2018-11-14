from random import randint

def pocet_pokusu():
    cislo = ''
    pokus = 1
    while cislo!= 6:
        cislo = randint(1,6)
        print("Vylosovane cislo:", cislo)
        print("Cislo pokusu:", pokus)
            
        if cislo != 6:
            pokus = pokus + 1
                
        else:
            return pokus
   
player_1 = pocet_pokusu()
vitez = "player_1"
vitezny_pokus = player_1
player_2 = pocet_pokusu()
if player_2 < vitezny_pokus:
    vitez = "player_2"
player_3 = pocet_pokusu()
if player_3 < vitezny_pokus:
    vitez = "player_3"
player_4 = pocet_pokusu()
if player_4 < vitezny_pokus:
    vitez = "player_4"

print(vitez)


