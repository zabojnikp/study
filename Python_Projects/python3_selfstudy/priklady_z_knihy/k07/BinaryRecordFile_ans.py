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
>>> import shutil
>>> import sys

>>> S = struct.Struct("<15s")
>>> fileA = os.path.join(tempfile.gettempdir(), "fileA.dat")
>>> fileB = os.path.join(tempfile.gettempdir(), "fileB.dat")
>>> for name in (fileA, fileB):
...    try:
...        os.remove(name)
...    except EnvironmentError:
...        pass

>>> brf = BinaryRecordFile(fileA, S.size)
>>> for text in ("Alpha", "Bravo", "Charlie", "Delta",
...        "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet",
...        "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
...        "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
...        "Whisky", "X-Ray", "Yankee", "Zulu"):
...    brf.append(S.pack(text.encode("utf8")))
>>> assert len(brf) == 26
>>> brf.append(S.pack(b"Extra at the end"))
>>> assert len(brf) == 27
>>> shutil.copy(fileA, fileB)
>>> del brf[12]
>>> del brf[0]
>>> del brf[24]
>>> assert len(brf) == 24, len(brf)
>>> brf.close()

>>> if ((os.path.getsize(fileA) + (3 * S.size)) !=
...        os.path.getsize(fileB)):
...    print("SELHÁNÍ#1: očekávané velikosti souborů jsou nesprávné")
...    sys.exit()

>>> shutil.copy(fileB, fileA)
>>> if os.path.getsize(fileA) != os.path.getsize(fileB):
...    print("SELHÁNÍ#2: očekávané velikosti souborů se liší")
...    sys.exit()

>>> for name in (fileA, fileB):
...    try:
...        os.remove(name)
...    except EnvironmentError:
...        pass

"""

import os
import struct
import tempfile


class BinaryRecordFile:

    def __init__(self, filename, record_size, auto_flush=True):
        """Binární soubor s náhodným přístupem, který se chová spíš jako seznam,
        kde každý je prvek objektem typu bytes nebo bytearray velikosti record_size.
        """
        self.__record_size = record_size
        mode = "w+b" if not os.path.exists(filename) else "r+b"
        self.__fh = open(filename, mode)
        self.auto_flush = auto_flush


    @property
    def record_size(self):
        "Velikost každého prvku"
        return self.__record_size


    @property
    def name(self):
        "Název souboru"
        return self.__fh.name


    def flush(self):
        """Kompletní zápis na disk
        Provádí se automaticky, má-li auto_flush hodnotu True
        """
        self.__fh.flush()


    def close(self):
        self.__fh.close()


    def append(self, record):
        """Přidá nový záznam"""
        assert isinstance(record, (bytes, bytearray)), \
               "binary data required"
        assert len(record) == self.record_size, (
            "záznam musí mít přesně {0} bajtů".format(
            self.record_size))
        self.__fh.seek(0, os.SEEK_END)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()


    def __setitem__(self, index, record):
        """Nastaví prvek na pozici index na zadaný záznam

        Indexová pozice může jít i za aktuální konec souboru.
        """
        assert isinstance(record, (bytes, bytearray)), \
               "vyžadována jsou binární data"
        assert len(record) == self.record_size, (
            "záznam musí mít přesně {0} bajtů".format(
            self.record_size))
        self.__seek_to_index(index)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()


    def __getitem__(self, index):
        """Vrátí prvek na zadané indexové pozici

        Pokud na zadané pozici žádný prvek není, vyvolá výjimku
        IndexError.
        """
        self.__seek_to_index(index)
        return self.__fh.read(self.record_size)
        

    def __seek_to_index(self, index):
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        offset = index * self.record_size
        if offset >= end:
            raise IndexError("na indexové pozice {0} není záznam".format(
                             index))
        self.__fh.seek(offset)


    def __delitem__(self, index):
        """Vymaže prvek na zadané indexové pozici a přesune
        následující záznamy.
        """
        length = len(self)
        for next in range(index + 1, length):
            self[index] = self[next]
            index += 1
        self.__fh.truncate((length - 1) * self.record_size)
        self.__fh.flush()


    def __len__(self):
        """Počet záznamů."""
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        return end // self.record_size


if __name__ == "__main__":
    import doctest
    doctest.testmod()
