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

import pickle


class Transaction:

    def __init__(self, amount, date, currency="EUR",
                 eur_conversion_rate=1, description=None):
        """
        >>> t = Transaction(100, "2008-12-09")
        >>> t.amount, t.currency, t.eur_conversion_rate, t.eur
        (100, 'EUR', 1, 100)
        >>> t = Transaction(250, "2009-03-12", "CZ", 0.26)
        >>> t.amount, t.currency, t.eur_conversion_rate, t.eur
        (250, 'CZ', 0.26, 65.0)
        """
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
    """
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_eur, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_eur, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "CZ", 0.26))
    >>> account.balance, account.all_eur, len(account)
    (168.0, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_eur, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_eur, len(newaccount)
    (168.0, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """

    def __init__(self, number, name):
        """Vytvoří nový účet se zadaným číslem a názvem

        Číslo se použije pro název souboru tohoto účtu.
        """
        self.__number = number
        self.__name = name
        self.__transactions = []
        

    @property
    def number(self):
        "Číslo účtu určené pouze pro čtení"
        return self.__number


    @property
    def name(self):
        """Název účtu

        Název lze změnit, protože slouží pouze pro lepší oreintaci lidí;
        skutečným identifikátorem je číslo účtu.
        """
        return self.__name

    @name.setter
    def name(self, name):
        assert len(name) > 3, "název účtu musí mít nejméně 4 znaky"
        self.__name = name


    def __len__(self):
        "Vrací počet transakcí"
        return len(self.__transactions)


    def apply(self, transaction):
        "Aplikuje (přidává) zadanou transakci do účtu"
        self.__transactions.append(transaction)


    @property
    def balance(self):
        "Vrací zůstatek v EUR"
        total = 0.0
        for transaction in self.__transactions:
            total += transaction.eur
        return total


    @property
    def all_eur(self):
        "Vrací True, jsou-li všechny transakce v EUR"
        for transaction in self.__transactions:
            if transaction.currency != "EUR":
                return False
        return True
         

    def save(self):
        "Uloží data účtu do souboru číslo_účtu.acc"
        fh = None
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(self.number + ".acc", "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()


    def load(self):
        """Načte data účtu ze souboru číslo_účtu.acc

        Všechna předchozí data budou ztracena.
        """
        fh = None
        try:
            fh = open(self.number + ".acc", "rb")
            data = pickle.load(fh)
            assert self.number == data[0], "číslo účtu nesedí"
            self.__name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
