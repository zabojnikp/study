slovnik = {}.fromkeys('ABCD', 3)
mnozina = set("ACX")
prunik = slovnik.keys() & mnozina
print(prunik)

sjednoceni = slovnik.keys() | mnozina
print(sjednoceni)

rozdil = slovnik.keys() - mnozina
print(rozdil)

synamtricky_rozdil = slovnik.keys() ^ mnozina
print(synamtricky_rozdil)