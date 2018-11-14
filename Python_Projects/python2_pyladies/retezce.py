retezec = "Hello, World"
print(retezec[:5])
print(retezec[-5:])
print(retezec[:5]+ retezec[-6:])
print(retezec.count('o'))
print(retezec.index('o'))
print(retezec.replace('e', 'a'))
print(retezec.startswith("h"))
vypis = 'Ahoj {jmeno}, vysledek je {cislo}.'.format(cislo=7, jmeno='Petro')
print(vypis)
retezec = 'čokoláda'
print(retezec[:4])
print(retezec[2:5])
print(retezec[-4:])
print(retezec[::-1])
print(retezec[::1])
name = input("What is your name?")[0]
surname = input("what is your surname?")[0]

print('Inicialy:', name.upper() + surname.upper())

def zamen(retezec, pozice, znak):
    return retezec.replace(retezec[pozice], znak)

print(zamen("palec", 0, "v"))
print(zamen('valec', 2, 'j'))