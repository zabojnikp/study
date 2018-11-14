import math

bod_a = [234, 34]
bod_b = [27, 114]

sirka = abs(bod_a[0] - bod_b[0])
delka = abs(bod_a[1] - bod_b[1])

vzdalenost = math.sqrt(sirka**2 + delka**2)
print(round(vzdalenost, 2))