def nacti_cislo(pole):
    while True:
        try:
            pozice = int(input('Kam chceš hrát? (0..19) '))
        except ValueError:
            print('To není číslo!')
        else:
            if pozice < 0 or pozice >= len(pole):
                print('Nemůžeš hrát venku z pole!')
            elif pole[pozice] != '-':
                print('Tam není volno!')
            else:
                break

    pole = pole[:pozice] + 'o' + pole[pozice + 1:]
    return pole


print(tah_hrace('-x----'))