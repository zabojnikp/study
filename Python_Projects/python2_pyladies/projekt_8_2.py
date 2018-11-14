# funkci, která dostane seznam souřadnic (párů čísel menších než 10) a vypíše je jako mapu. 

def create_table(rows, columns):
    list_rows = []
    for i in range(columns):
        list_rows.append(rows * ' . ')
        
    return '\n'.join(list_rows)

print(create_table(10, 10))

x, o = 'xo'
jedna, dva, tri = [1, 2, 3]
print(x)
print(o)
print(jedna)
print(tri)
def podil_a_zbytek(a, b):
    return a // b, a % b

podil, zbytek = podil_a_zbytek(17, 5)
print(podil)
print(zbytek)

osoby = 'máma', 'teta', 'babička'
for osoba in osoby:
    print(osoba)
print('První je {}'.format(osoby[0]))

seznam_dvojic = []
for i in range(10):
    # `append` bere jen jeden argument; dáme mu jednu dvojici
    seznam_dvojic.append((i, i**2))
print(seznam_dvojic)

osoby = 'máma', 'teta', 'babička', 'vrah'
vlastnosti = 'hodná', 'milá', 'laskavá', 'zákeřný'
for osoba, vlastnost in zip(osoby, vlastnosti):
    print('{} je {}'.format(osoba, vlastnost))

prvocisla = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for i, prvocislo in enumerate(prvocisla):
    print('Pvočíslo č.{} je {}'.format(i, prvocislo))