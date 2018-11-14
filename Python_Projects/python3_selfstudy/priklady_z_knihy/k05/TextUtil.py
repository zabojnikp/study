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

"""
Tento modul nabízí několik funkcí pro manipulaci s řetězci.

>>> is_balanced("(Python (není (jako (lisp))))")
True
>>> shorten("Velká křižovatka", 10)
'Velká k...'
>>> simplify(" nějaký    text    s  nadbytečnými  mezerami  ")
'nějaký text s nadbytečnými mezerami'
"""

import string


def is_balanced(text, brackets="()[]{}<>"):
    """Vrátí hodnotu True, jsou-li všechny závorky v textu vyváženy.

    U každé dvojice závorek musejí být levé a pravé znaky odlišné.

    >>> is_balanced("úplně bez závorek")
    True
    >>> is_balanced("<b>tučně</b>")
    True
    >>> is_balanced("[<b>(někde {něco}) máme</b>]")
    True
    >>> is_balanced("<b>[sem (to {nejspíš}) nepatří}]</b>")
    False
    >>> is_balanced("(není (<značka>(jako) (jiná)</značka>)")
    False
    """
    counts = {}
    left_for_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "znaky závorek se musejí lišit"
        counts[left] = 0
        left_for_right[right] = left
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1
    return not any(counts.values())


def shorten(text, length=25, indicator="..."):
    """Vrátí text nebo ořezanou kopii s připojeným indikátorem

    text je libovolný řetězec; length je maximální délka vráceného
    řetězce (včetně případného indikátoru); indikátor je řetězec přidaný
    na konec, který signalizuje, že text byl zkrácen
    
    >>> shorten("Druhá varieta")
    'Druhá varieta'
    >>> shorten("Hlasy z druhé strany ulice", 17)
    'Hlasy z druhé ...'
    >>> shorten("Rádio Malý Škuner", 10, "*")
    'Rádio Mal*'
    """
    if len(text) > length:
        text = text[:length - len(indicator)] + indicator
    return text


def simplify(text, whitespace=string.whitespace, delete=""):
    r"""Vrátí text s vícenásobnými mezerami zredukovanými do jediné mezery

    Parametr whitespace je řetězec znaků, z nichž každý 
    je považován za mezeru.
    Není-li paramtr delete prázdný, měl by obsahovat řetězec, jehož 
    znaky se vyhledají ve výsledném řetězci a odstraní.

    >>> simplify(" tohle    a\n také\t tamto")
    'tohle a také tamto'
    >>> simplify("  Vejce   a.s.\n")
    'Vejce a.s.'
    >>> simplify("  Vejce   a.s.\n", delete=",;:.")
    'Vejce as'
    >>> simplify(" nesamohláskový ", delete="aáeiouyý")
    'nsmhlskv'
    """
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        result.append(word)
    return " ".join(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
