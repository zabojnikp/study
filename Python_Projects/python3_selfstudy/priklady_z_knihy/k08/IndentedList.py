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


def indented_list_sort(indented_list, indent="    "):
    """Vrátí abecedně seřazenou kopii zadaného seznamu

    Seznam s odsazením je sezanam řetězců v hierarchii odsazení
    použité pro označení podřízených prkvů.
    Parametr indent stanoví znaky, které tvoří jednu úroveň odsazení.

    Funkce zkopíruje seznam a vrátí jej abecedně seřazení bez oheldu na
    velikost písmen s tím, že podřízené prvky se seřadí
    pod svými rodiči, což rekurzivně pokračuje do libovolné hloubky.

    >>> indented_list = ["M", " MX", " MG", "D", " DA", " DF",\
    "  DFX", "  DFK", "  DFB", " DC", "K", "X", "H", " HJ",\
    " HB", "A"]
    >>> 
    >>> indented_list = indented_list_sort(indented_list, " ")
    >>> indented_list[:8]
    ['A', 'D', ' DA', ' DC', ' DF', '  DFB', '  DFK', '  DFX']
    >>> indented_list[8:]
    ['H', ' HB', ' HJ', 'K', 'M', ' MG', ' MX', 'X']
    """
    KEY, ITEM, CHILDREN = range(3)

    def add_entry(level, key, item, children):
        if level == 0:
            children.append((key, item, []))
        else:
            add_entry(level - 1, key, item, children[-1][CHILDREN])

    def update_indented_list(entry):
        indented_list.append(entry[ITEM])
        for subentry in sorted(entry[CHILDREN]):
            update_indented_list(subentry)

    entries = []
    for item in indented_list:
        level = 0
        i = 0
        while item.startswith(indent, i):
            i += len(indent)
            level += 1
        key = item.strip().lower()
        add_entry(level, key, item, entries)

    indented_list = []
    for entry in sorted(entries):
        update_indented_list(entry)
    return indented_list


def indented_list_sort_local(indented_list, indent="    "):
    """
    Při zadání seznam s odsazením, tj. seznamu prvků s odsazenými
    podprky, seřadí tyto prvky a podprvky v rámci každého prvku
    (při čemž pokračuje rekurzivně do hloubky) podle abecedy 
    bez ohledu na velikost písmen.

    >>> indented_list = ["M", " MX", " MG", "D", " DA", " DF", "  DFX", \
    "  DFK", "  DFB", " DC", "K", "X", "H", " HJ", " HB", "A"]
    >>> 
    >>> indented_list = indented_list_sort_local(indented_list, " ")
    >>> indented_list[:8]
    ['A', 'D', ' DA', ' DC', ' DF', '  DFB', '  DFK', '  DFX']
    >>> indented_list[8:]
    ['H', ' HB', ' HJ', 'K', 'M', ' MG', ' MX', 'X']
    """
    KEY, ITEM, CHILDREN = range(3)

    def add_entry(key, item, children):
        nonlocal level
        if level == 0:
            children.append((key, item, []))
        else:
            level -= 1
            add_entry(key, item, children[-1][CHILDREN])

    def update_indented_list(entry):
        indented_list.append(entry[ITEM])
        for subentry in sorted(entry[CHILDREN]):
            update_indented_list(subentry)

    entries = []
    for item in indented_list:
        level = 0
        i = 0
        while item.startswith(indent, i):
            i += len(indent)
            level += 1
        key = item.strip().lower()
        add_entry(key, item, entries)

    indented_list = []
    for entry in sorted(entries):
        update_indented_list(entry)
    return indented_list


if __name__ == "__main__":
    before = ["Nekovy",
    "    Vodík",
    "    Uhlík",
    "    Dusík",
    "    Kyslík",
    "Přechodné prvky",
    "    Lanthanoidy",
    "        Cerium",
    "        Europium",
    "    Aktinoidy",
    "        Uran",
    "        Curium",
    "        Plutonium",
    "Alkalické kovy",
    "    Lithium",
    "    Sodík",
    "    Draslík"]
    result1 = indented_list_sort(before)
    result2 = indented_list_sort_local(before)
    after = ["Alkalické kovy",
    "    Draslík",
    "    Lithium",
    "    Sodík",
    "Nekovy",
    "    Dusík",
    "    Kyslík",
    "    Uhlík",
    "    Vodík",
    "Přechodné prvky",
    "    Aktinoidy",
    "        Curium",
    "        Plutonium",
    "        Uran",
    "    Lanthanoidy",
    "        Cerium",
    "        Europium"]
    assert result1 == result2 == after

    import doctest
    doctest.testmod()
