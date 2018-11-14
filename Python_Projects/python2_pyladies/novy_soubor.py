with open ("novy-soubor.txt", mode='w', encoding='utf-8') as soubor:
  soubor.write("prvni radek\n")
  soubor.write("druhy radek\n")

with open('novy-soubor.txt', mode="a", encoding='utf-8') as soubor:
    soubor.write("treti radek\n")

soubor = open('novy-soubor.txt', encoding ='utf-8')
try:
    obsah = soubor.read()
    print(obsah)
finally:
    soubor.close()