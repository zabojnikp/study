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

import datetime
import os
import pickle
import shelve
import sys
import tempfile
import xml.etree.ElementTree
import xml.parsers.expat
import xml.sax.saxutils
import Console


DISPLAY_LIMIT = 20


def main():
    functions = dict(p=add_dvd, u=edit_dvd, v=list_dvds,
                     o=remove_dvd, i=import_, e=export, k=quit)
    filename = os.path.join(os.path.dirname(__file__), "dvds.dbm")
    db = None
    try:
        db = shelve.open(filename, protocol=pickle.HIGHEST_PROTOCOL)
        action = ""
        while True:
            print("\nNosiče DVD ({0})".format(os.path.basename(filename)))
            if action != "l" and 1 <= len(db) < DISPLAY_LIMIT:
                list_dvds(db)
            else:
                print("{0} nosičů dvd".format(len(db)))
            print()
            menu = ("(P)řidat  (U)pravit  (V)ypsat  (O)dstranit  (I)mportovat  "
                    "(E)xportovat  (K)onec"
                    if len(db) else "(P)řidat  (I)mportovat  (K)onec")
            valid = frozenset("puvoiek" if len(db) else "pik")
            action = Console.get_menu_choice(menu, valid,
                                        "v" if len(db) else "p", True)
            functions[action](db)
    finally:
        if db is not None:
            db.close()


def add_dvd(db):
    title = Console.get_string("Název", "název")
    if not title:
        return
    director = Console.get_string("Režisér", "režisér")
    if not director:
        return
    year = Console.get_integer("Rok", "rok", minimum=1896,
                               maximum=datetime.date.today().year)
    duration = Console.get_integer("Délka (v minutách)", "minuty",
                                   minimum=0, maximum=60*48)
    db[title] = (director, year, duration)
    db.sync()
    

def edit_dvd(db):
    old_title = find_dvd(db, "edit")
    if old_title is None:
        return
    title = Console.get_string("Název", "název", old_title)
    if not title:
        return
    director, year, duration = db[old_title]
    director = Console.get_string("Režisér", "režisér", director)
    if not director:
        return
    year = Console.get_integer("Rok", "rok", year, 1896,
                               datetime.date.today().year)
    duration = Console.get_integer("Délka (v minutách)", "minuty",
                                   duration, minimum=0, maximum=60*48)
    db[title] = (director, year, duration)
    if title != old_title:
        del db[old_title]
    db.sync()
    

def list_dvds(db):
    start = ""
    if len(db) > DISPLAY_LIMIT:
        start = Console.get_string("Vypsat ty, které začínají na "
                                   "[Enter=vše]", "start")
    print()
    for title in sorted(db, key=str.lower):
        if not start or title.lower().startswith(start.lower()):
            director, year, duration = db[title]
            print("{title} ({year}) {duration} minut, režie "
                  "{director}".format(**locals()))
    

def remove_dvd(db):
    title = find_dvd(db, "remove")
    if title is None:
        return
    ans = Console.get_bool("Odstranit {0}?".format(title), "ne")
    if ans:
        del db[title]
        db.sync()
    

def import_(db):
    filename = Console.get_string("Importovat z", "název souboru")
    if not filename:
        return
    try:
        tree = xml.etree.ElementTree.parse(filename)
    except (EnvironmentError,
            xml.parsers.expat.ExpatError) as err:
        print("CHYBA:", err)
        return
    db.clear()
    for element in tree.findall("dvd"):
        try:
            year = int(element.get("year"))
            duration = int(element.get("duration"))
            director = element.get("director")
            title = element.text.strip()
            db[title] = (director, year, duration)
        except ValueError as err:
            print("CHYBA:", err)
            return
    print("Importováno {0} nosičů dvd".format(len(db)))
    db.sync()

    
def export(db):
    filename = os.path.join(tempfile.gettempdir(), "dvds.xml")
    with open(filename, "w", encoding="utf8") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        fh.write("<dvds>\n")
        for title in sorted(db, key=str.lower):
            director, year, duration = db[title]
            fh.write('<dvd year="{year}" duration="{duration}" '
                     'director={0}>'.format(xml.sax.saxutils.
                     quoteattr(director), **locals()))
            fh.write(xml.sax.saxutils.escape(title))
            fh.write("</dvd>\n")
        fh.write("</dvds>\n")
        fh.close()
    print("{0} nosičů dvd exportováno do {1}".format(
          len(db), filename))


def quit(db):
    print("Uloženo {0} nosičů dvd".format(len(db)))
    db.close()
    sys.exit()


def find_dvd(db, message):
    message = "(Začátek) názvu " + message
    while True:
        matches = []
        start = Console.get_string(message, "název")
        if not start:
            return None
        for title in db:
            if title.lower().startswith(start.lower()):
                matches.append(title)
        if len(matches) == 0:
            print("Nemohu najít žádné nosiče DVD začínající na", start)
            continue
        elif len(matches) == 1:
            return matches[0]
        elif len(matches) > DISPLAY_LIMIT:
            print("Na {0} začíná příliš mnoho nosičů DVD; zkuste zadat "
                  "větší část názvu".format(start))
            continue
        else:
            matches = sorted(matches, key=str.lower)
            for i, match in enumerate(matches):
                print("{0}: {1}".format(i + 1, match))
            which = Console.get_integer("Číslo (nebo 0 pro zrušení)",
                            "číslo", minimum=1, maximum=len(matches))
            return matches[which - 1] if which != 0 else None

main()
