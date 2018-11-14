osoba = {
    'jmeno': "Petra", 
    'prijmeni': "zabojnikova", 
    'mesto': "Zlin", 
    'cisla':[1,2,3]
    }
print(osoba['prijmeni'])
osoba['prijmeni'] = 'Zabojnikova'
print(osoba['prijmeni'])
osoba['jazyk'] = 'Python'
print(osoba)
del osoba['cisla']
print(osoba)

for key in osoba:
    print(key)

for value in osoba.values():
    print(value)

for key, value in osoba.items():
    print(key, ":", value)
    print('{}:{}'.format(key, value))

cisla = {
    'Maruška': '153 85283',
    'Terka': '237 26505',
    'Renata': '385 11223',
    'Michal': '491 88047',
}

barvy = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

popisy_funkci = {'len': 'délka', 'str': 'řetězec', 'dict': 'slovník'}
for klic in popisy_funkci:
    print(klic)

for values in popisy_funkci.values():
    print(values)

for klic, hodnota in popisy_funkci.items():
    print('{}: {}'.format(klic, hodnota))


barvy_po_tydnu = dict(barvy)
for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'černo-hnědo-' + barvy_po_tydnu[klic]
print(barvy['jablko'])
print(barvy_po_tydnu['jablko'])

data = [(1, 'jedna'), (2, 'dva'), (3, 'tři')]
nazvy_cisel = dict(data)
print(nazvy_cisel)

data_2 = dict(len="jedna", hallo="dva")
print(data_2)

barvy = { 
    'jablko': 'červená',
    'meloun': 'zelená'
 }

dalsi_barvy = dict(hruska='zluta', švestka='modrá')

hodnota = barvy.get('jablko')
print(hodnota)

hodnota = barvy.get('jabklo', 'cervena')
print(hodnota)

hodnota = barvy.pop('jablko')
print(hodnota)
print(barvy)

ovoce, barva = barvy.popitem()
print(ovoce, barva)
print(barvy)

barvy['angrest'] = 'zelená'
print(barvy)
del barvy['angrest']
print(barvy)

barvy.update(dalsi_barvy)
print(barvy)

barvy.setdefault('angrešt', 'modra')
print(barvy)


barvy['angrešt'] = 'zelená'
print(barvy)

while barvy:
 ovoce, barva = barvy.popitem()
 print('{}: {}'.format(
 ovoce, barva))

print(barvy)