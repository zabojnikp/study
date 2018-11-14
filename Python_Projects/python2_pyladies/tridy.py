class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mnau mnau! {} mi chutna!".format(self.jmeno, jidlo))

mourek = Kotatko('Mourek')
mourek.zamnoukej()
mourek.snez('ryba')

class Kocka:
    def __init__(self):
        self.pocet_zivotu = 9

    def zamnoukej(self):
        print('Mnau')

    def je_ziva(self):
        return self.pocet_zivotu > 0
    
    def uber_zivot(self):
        if not self.je_ziva():
            print("nemuzes ubrat zivot mrtve kocce")
        else:
            self.pocet_zivotu = self.pocet_zivotu - 1
    
    def snez(self, jidlo):
        if not self.je_ziva():
            print("Je zbytecne krmit mrtvou kocku!")
            return
        if jidlo == 'ryba' and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print("kocce se obnovil jeden zivot")
        else:
            print("kocka se krmi")

micka = Kocka()
micka.zamnoukej()
micka.je_ziva()
micka.uber_zivot()
micka.snez("ryba")