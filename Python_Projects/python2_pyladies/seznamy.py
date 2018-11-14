
cisla = [1, 2, 3, 4, 5, 6, 7]
print(cisla)
for cislo in cisla:
    print(cislo)

seznam = [1, 'abc', True, None, range(10), len]
print(seznam)
print(cisla[2:-4])
cisla.append(8)
print(cisla)

dalsi_cisla = [9, 10, 11]
cisla.extend(dalsi_cisla)
print(cisla)

seznam = []
seznam.extend('abcdef')
seznam.extend(range(10))
print(seznam)

cisla = [1, 0, 3, 4]
cisla[1] = 2
print(cisla)

cisla = [1, 2, 3, 4]
cisla[1:-1] = [6, 5]
print(cisla)

cisla = [1, 2, 3, 4]
cisla[1:-1] = [0, 0, 0, 0, 0, 0]
print(cisla)
cisla[1:-1] = []
print(cisla)

cisla = [1, 2, 3, 4, 5, 6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)

cisla = [1, 2, 3, 'abc', 4, 5, 6, 12]
posledni = cisla.pop()
print(posledni)
print(cisla)

cisla.remove('abc')
print(cisla)

cisla.clear()
print(cisla)

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort(reverse=True)
print(seznam)

melodie = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(melodie)

print(len(melodie))         # Délka seznamu
print(melodie.count('D'))   # Počet 'D' v seznamu
print(melodie.index('D'))   # Číslo prvního 'D'
print('D' in melodie)
print('DE' in melodie)
print(melodie.count('DE'))

abeceda = list('abcdefghijklmnopqrstuvwxyz')
cisla = list(range(100))
print(abeceda)
print(cisla)

a = [1, 2, 3]
b = list(a)

print(b)
a.append(4)
print(b)

mocniny_dvou = []
for cislo in range(10):
    mocniny_dvou.append(2 ** cislo)
print(mocniny_dvou)

balicek = []
for barva in '♠', '♥', '♦', '♣':  # (Na Windows použij textová jména)
    for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        balicek.append(str(hodnota) + barva)
print(balicek)

retezec = ""
if retezec:
    print("v seznamu neco je")

else:
    print("v seznamu nic neni")