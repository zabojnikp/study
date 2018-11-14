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

import os


YES = frozenset({"a", "A", "ano", "Ano", "ANO"})


def main():
    dirty = False
    items = []

    filename, items = choose_file()
    if not filename:
        print("Zrušeno")
        return

    while True:
        print("\nStrážce seznamu\n")
        print_list(items)
        choice = get_choice(items, dirty)

        if choice in "Pp":
            dirty = add_item(items, dirty)
        elif choice in "Vv":
            dirty = delete_item(items, dirty)
        elif choice in "Uu":
            dirty = save_list(filename, items)
        elif choice in "Kk":
            if (dirty and (get_string("Uložit provedené změny (a/n)",
                                      "ano/ne", "a") in YES)):
                save_list(filename, items, True)
            break


def choose_file():
    enter_filename = False
    print("\nStrážce seznamu\n")
    files = [x for x in os.listdir(".") if x.endswith(".lst")]
    if not files:
        enter_filename = True
    if not enter_filename:
        print_list(files)
        index = get_integer("Zvolte číslo souboru (nebo 0 pro vytoření "
                            "nového)", "number", maximum=len(files),
                            allow_zero=True)
        if index == 0:
            enter_filename = True
        else:
            filename = files[index - 1]
            items = load_list(filename)
    if enter_filename:
        filename = get_string("Zadejte název souboru", "filename")
        if not filename.endswith(".lst"):
            filename += ".lst"
        items = []
    return filename, items



def print_list(items):
    if not items:
        print("-- v seznamu nejsou žádné prvky --")
    else:
        width = 1 if len(items) < 10 else 2 if len(items) < 100 else 3
        for i, item in enumerate(items):
            print("{0:{width}}: {item}".format(i + 1, **locals()))
    print()


def get_choice(items, dirty):
    while True:
        if items:
            if dirty:
                menu = "[P]řidat  [V]ymazat  [U]ložit  [K]onec"
                valid_choices = "PpVvUuKk"
            else:
                menu = "[P]řidat  [V]ymazat  [K]onec"
                valid_choices = "PpVvKk"
        else:
            menu = "[P]řidat  [K]onec"
            valid_choices = "PpKk"
        choice = get_string(menu, "choice", "p")

        if choice not in valid_choices:
            print("CHYBA: neplatná volba--zadejte některou z těchto možností: '{0}'".format(
                  valid_choices))
            input("Pro pokračování stiskněte klávesu Enter...")
        else:
            return choice


def add_item(items, dirty):
    item = get_string("Přidat prvek", "item")
    if item:
        items.append(item)
        items.sort(key=str.lower)
        return True
    return dirty


def delete_item(items, dirty):
    index = get_integer("Vymazat prvek (nebo 0 pro zrušení mazání)",
                        "number", maximum=len(items),
                        allow_zero=True)
    if index != 0:
        del items[index - 1]
        return True
    return dirty


def load_list(filename):
    items = []
    fh = None
    try:
        for line in open(filename, encoding="utf8"):
            items.append(line.rstrip())
    except EnvironmentError as err:
        print("CHYBA: nemohu načíst {0}: {1}".format(filename, err))
        return []
    finally:
        if fh is not None:
            fh.close()
    return items


def save_list(filename, items, terminating=False):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        fh.write("\n".join(items))
        fh.write("\n")
    except EnvironmentError as err:
        print("CHYBA: nemohu uložit {0}: {1}".format(filename, err))
        return True
    else:
        print("Seznam byl uložen do {0}, celkem uloženo prvků: {1}".format(filename, len(items)))
        if not terminating:
            input("Pro pokračování stiskněte klávesu Enter...")
        return False
    finally:
        if fh is not None:
            fh.close()


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} nesmí být prázdná".format(
                                     name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} musí mít nejméně "
                        "{minimum_length} a nejvíce "
                        "{maximum_length} znaků".format(
                        **locals()))
            return line
        except ValueError as err:
            print("CHYBA", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} nesmí být 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} musí být mezi {minimum} "
                        "a {maximum} včetně {0}".format(
                        " (nebo 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("CHYBA", err)
        except ValueError as err:
            print("CHYBA: {0} musí být celé číslo".format(name))


main()
