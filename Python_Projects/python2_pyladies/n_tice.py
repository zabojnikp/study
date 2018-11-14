osoby = 'máma', 'teta', 'babička'

for osoba in osoby:
    print(osoba)

print('První je {}'.format(osoby[0]))

seznam_dvojic = []
for i in range(10):
    # `append` bere jen jeden argument; dáme mu jednu dvojici
    seznam_dvojic.append((i, i**2))

print(seznam_dvojic)

def podil_a_zbytek(a, b):
    return a // b, a % b

print(podil_a_zbytek(6, 2))

osoby = 'máma', 'teta', 'babička', 'vrah'
vlastnosti = 'hodná', 'milá', 'laskavá', 'zákeřný'
for osoba, vlastnost in zip(osoby, vlastnosti):
    print('{} je {}!'.format(osoba, vlastnost))

prvocisla = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for i, prvocislo in enumerate(prvocisla):
    print('Pvočíslo č.{} je {}'.format(i, prvocislo))