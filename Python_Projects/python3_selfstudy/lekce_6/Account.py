#!/usr/bin/env python3
# Copyright (c) 2008-9 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
'''
Dokumentacni retezec s testama

bla bla bla

'''
import pickle
class Transaction:
    """
        >>> t = Transaction(100, "2008-12-09")
        >>> t.amount, t.currency, t.eur_conversion_rate, t.eur
        (100, 'EUR', 1, 100)
        >>> t = Transaction(250, "2009-03-12", "CZ", 0.26)
        >>> t.amount, t.currency, t.eur_conversion_rate, t.eur
        (250, 'CZ', 0.26, 65.0)
    """
    def __init__(self, amount, date, currency = "EUR", eur_conversion_rate = 1, description = None):
        self.__amount = amount
        self.__date = date
        self.__description = description
        self.__currency = currency
        self.__eur_conversion_rate = eur_conversion_rate
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def date(self):
        return self.__date

    @property
    def description(self):
        return self.__description
    
    @property
    def currency(self):
        return self.__currency
    
    @property
    def eur_conversion_rate(self):
        return self.__eur_conversion_rate
    
    @property
    def eur(self):
        return self.__amount * self.__eur_conversion_rate

class Account:
    def __init__(self, number, name):
        "Vytvoří nový účet se zadaným číslem a názvem"
        self.__number = number
        self.__name = name
        self.__transactions = []

    @property
    def number(self):
        "Číslo účtu určené pouze pro čtení"
        return self.__number

    @property
    def name(self):
        "Název účtu"
        return self.__name

    @name.setter
    def name(self, name):
        "umozni uzivateli nastavit jmeno"
        assert len(name) > 3, "musi byt minimalne 4 znaky"
        self.__name = name
    
    def __len__(self):
        "vraci pocet transakci"
        return len(self.__transactions)
    
    def apply(self, transaction):
        "metoda pro pridani transakce"
        self.__transactions.append(transaction)

    @property
    def balance(self):
        "vlastnost ktera vraci zustatek v eurech"
        total = 0
        for transaction in self.__transactions:
            total += transaction.eur
        return total
    
    @property
    def all_eur(self):
        "vraci hodnotu True jsou-li vsechny transakce v EUR"
        for transaction in self.__transactions:
            if transaction.currency != "EUR":
                return False
        return True
    
    def save(self):
        "Uloží data účtu do souboru číslo_účtu.acc"
        
        fh = None
        filename = "{0}.acc".format(self.__number)
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise EnvironmentError(str(err))
        finally:
            if fh is not None:
                fh.close()
    
    def load(self):
        "Načte data účtu ze souboru číslo_účtu.acc"
        
        fh = None
        filename = "{0}.acc".format(self.__number)
        try:
            fh = open(filename, "rb")
            data = pickle.load(fh)
            assert self.number == data[0], "číslo účtu nesedí"
            self.__name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise EnvironmentError(str(err))
        finally:
            if fh is not None:
                fh.close()
        return data

if __name__ == "__main__":
    import doctest
    doctest.testmod()