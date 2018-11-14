import math
print(math.sqrt(2))

barva_travy = 'zelena'
pocet_kotatek = 28

def popis_stav():
    return 'Trava je {barva}. Prohani se po ni {pocet} kotatek'.format(
        barva=barva_travy, pocet=pocet_kotatek)

print('Louka je zelena!')