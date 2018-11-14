strana = int(input('Zadej cislo: '))
if strana >= 0:
    print("Obvod čtverce se stranou ", strana, " cm je ", 4 * strana, "cm")
    print("Obsah čtverce se stranou ", strana, " cm je ", strana ** 2, "cm")
else:
    print("strana musi byt kladna")


vek = int(input("kolik je ti let?"))
if vek >= 65:
    print("duchodce")

elif vek >= 18:
    print('dospely')

elif vek >= 1:
    print('dite')

elif vek < 1:
    print("novorozenec")

else:
    print('mimo radar')
