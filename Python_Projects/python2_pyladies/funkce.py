from math import pi
obsah = 0
a = 30

def obsah_elipsy(a, b):
    obsah = pi * a * b  # Přiřazení do `obsah`
    a = a + 3  # Přiřazení do `a`
    return obsah

print(obsah_elipsy(a, 20))
print(obsah)
print(a)