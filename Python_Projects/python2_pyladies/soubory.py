def iniciala():
    """Vrátí první písmeno v daném souboru."""
    with open('basnicka.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()
        return obsah[0]

print(iniciala())

with open('druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
    soubor.write("prvni radek\n")
    soubor.write("druhy radek\n")
    print("nase stare hodiny", file=soubor)