class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutna!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def snez(self, jidlo):
        print("({} na {} chvili fascinovane kouka)".format(self.jmeno, jidlo))
        #super().snez(jidlo)

    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))

class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))

class Hadatko(Zviratko):
    def __init__(self, jmeno):
        self.jmeno = jmeno
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')



standa = Hadatko('Stanislav')
standa.snez('mys')
micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('mys')
azorek.snez('kost')

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutna!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))


class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))

zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.snez('flakota')