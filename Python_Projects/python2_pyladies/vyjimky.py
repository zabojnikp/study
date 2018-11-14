## -*- coding: utf-8 -*-
while True:
    try:
        strana = float(input('Zadej stranu čtverce v centimetrech: '))
    except NameError:
        print('To nebylo číslo!')
    else:
        if strana <= 0:
            print('To nedává smysl!')
        else:
            break

print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')

VELIKOST_POLE = 20

def over_cislo(cislo):
    if 0 <= cislo < VELIKOST_POLE:
        print('OK!')
    else:
        raise ValueError('Čislo {n} není v poli!'.format(n=cislo))

print(over_cislo(-1))