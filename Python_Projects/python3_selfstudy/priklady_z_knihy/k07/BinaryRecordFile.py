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
>>> for i, text in enumerate(("Alpha", "Bravo", "Charlie", "Delta",
...        "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet",
...        "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
...        "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
...        "Whisky", "X-Ray", "Yankee", "Zulu")):
...    brf[i] = S.pack(text.encode("utf8"))
>>> assert len(brf) == 26
>>> brf[len(brf) + 2] = S.pack(b"Extra at the end")
>>> assert len(brf) == 29
>>> shutil.copy(fileA, fileB)
>>> del brf[12]
>>> assert len(brf) == 29
>>> brf.compact()
>>> assert len(brf) == 26
>>> brf.close()

>>> if ((os.path.getsize(fileA) + 3 + (3 * S.size)) !=
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

>>> filename =  os.path.join(tempfile.gettempdir(), "test.dat")
>>> if os.path.exists(filename): os.remove(filename)
>>> S = struct.Struct("<8s")
>>> test = BinaryRecordFile(filename, S.size)
>>> test[0] = S.pack(b"Alpha")
>>> test[1] = S.pack(b"Bravo")
>>> test[2] = S.pack(b"Charlie")
>>> test[3] = S.pack(b"Delta")
>>> test[4] = S.pack(b"Echo")
>>> test.inplace_compact()  # žádný prázdný či vymazaný
>>> test.close()
>>> os.path.getsize(filename)
45
>>> test = BinaryRecordFile(filename, S.size)
>>> len(test)
5
>>> for index in range(len(test)):
...     del test[index]
>>> test.inplace_compact()  # všechny prázdné či vymazané
>>> test.close()
>>> os.path.getsize(filename)
0
>>> test = BinaryRecordFile(filename, S.size)
>>> test[0] = S.pack(b"Alpha")
>>> test[1] = S.pack(b"Bravo")
>>> test[2] = S.pack(b"Charlie")
>>> test[3] = S.pack(b"Delta")
>>> test[4] = S.pack(b"Echo")
>>> del test[2]
>>> del test[4]
>>> del test[3]
>>> test.inplace_compact()  # prázdné či vymazané na konci
>>> test.close()
>>> os.path.getsize(filename)
18
>>> test = BinaryRecordFile(filename, S.size)
>>> test[0] = S.pack(b"Alpha")
>>> test[1] = S.pack(b"Bravo")
>>> test[2] = S.pack(b"Charlie")
>>> test[3] = S.pack(b"Delta")
>>> test[4] = S.pack(b"Echo")
>>> del test[0]
>>> del test[2]
>>> del test[3]
>>> test.inplace_compact()  # prázdné či vymazané uvnitř
>>> test.close()
>>> os.path.getsize(filename)
18
>>> os.remove(filename)
"""

import os
import struct
import tempfile


_DELETED = b"\x01"
_OKAY = b"\x02"


class BinaryRecordFile:

    def __init__(self, filename, record_size, auto_flush=True):
        """Binární soubor s náhodným přístupem, který se chová spíš jako seznam,
        kde každý je prvek objektem typu bytes nebo bytearray velikosti record_size.
        """
        self.__record_size = record_size + 1
        mode = "w+b" if not os.path.exists(filename) else "r+b"
        self.__fh = open(filename, mode)
        self.auto_flush = auto_flush


    @property
    def record_size(self):
        "Velikost každého prvku"
        return self.__record_size - 1


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


    def __setitem__(self, index, record):
        """Nastaví prvek na pozici index na zadaný záznam

        Indexová pozice může jít i za aktuální konec souboru.
        """
        assert isinstance(record, (bytes, bytearray)), \
               "vyžadována jsou binární data"
        assert len(record) == self.record_size, (
            "záznam musí mít přesně {0} bajtů".format(
            self.record_size))
        self.__fh.seek(index * self.__record_size)
        self.__fh.write(_OKAY)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()


    def __getitem__(self, index):
        """Vrátí prvek na zadané indexové pozici

        Pokud na zadané pozici žádný prvek není, vyvolá výjimku
        IndexError.
        Pokud byl prvek na zadané pozici vymazán, vrátí None.
        """
        self.__seek_to_index(index)
        state = self.__fh.read(1)
        if state != _OKAY:
            return None
        return self.__fh.read(self.record_size)
        

    def __seek_to_index(self, index):
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        offset = index * self.__record_size
        if offset >= end:
            raise IndexError("na indexové pozice {0} není záznam".format(
                             index))
        self.__fh.seek(offset)


    def __delitem__(self, index):
        """Vymaže prvek na zadané indexové pozici.

        Viz undelete()
        """
        self.__seek_to_index(index)
        state = self.__fh.read(1)
        if state != _OKAY:
            return
        self.__fh.seek(index * self.__record_size)
        self.__fh.write(_DELETED)
        if self.auto_flush:
            self.__fh.flush()


    def undelete(self, index):
        """Zruší vymazání prvku na zadané indexové pozici.

        Je-li prvek vymazán, lze jeho vymazání zrušit, pokud ovšem 
        nebyla zavolána metoda compact() (nebo inplace_compact()).
        """
        self.__seek_to_index(index)
        state = self.__fh.read(1)
        if state == _DELETED:
            self.__fh.seek(index * self.__record_size)
            self.__fh.write(_OKAY)
            if self.auto_flush:
                self.__fh.flush()
            return True
        return False


    def __len__(self):
        """Počet pozic pro záznamy.

        Jedná se o maximální počet záznamů, které mohou v daném
        okamžiku existovat. Jejich skutečný může být nižší, protože
        některé záznamy mohou být vymazány. Po zavolání metody compact() 
        nebo inplace_compact()) se jedná o skutečný počet záznamů.
        """
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        return end // self.__record_size


    def compact(self, keep_backup=False):
        """Zruší prázdné nebo vymazané záznamy"""
        compactfile = self.__fh.name + ".$$$"
        backupfile = self.__fh.name + ".bak"
        self.__fh.flush()
        self.__fh.seek(0)
        fh = open(compactfile, "wb")
        while True:
            data = self.__fh.read(self.__record_size)
            if not data:
                break
            if data[:1] == _OKAY:
                fh.write(data)
        fh.close()
        self.__fh.close()

        os.rename(self.__fh.name, backupfile)
        os.rename(compactfile, self.__fh.name)
        if not keep_backup:
            os.remove(backupfile)
        self.__fh = open(self.__fh.name, "r+b")


    def inplace_compact(self):
        """Zruší prázdné a vymazané záznamy na místě při zachování
        původního pořadí
        """
        index = 0
        length = len(self)
        while index < length:
            self.__seek_to_index(index)
            state = self.__fh.read(1)
            if state != _OKAY:
                for next in range(index + 1, length):
                    self.__seek_to_index(next)
                    state = self.__fh.read(1)
                    if state == _OKAY:
                        self[index] = self[next]
                        del self[next]
                        break
                else:
                    break
            index += 1
        self.__seek_to_index(0)
        state = self.__fh.read(1)
        if state != _OKAY:
            self.__fh.truncate(0)
        else:
            limit = None
            for index in range(len(self) - 1, 0, -1):
                self.__seek_to_index(index)
                state = self.__fh.read(1)
                if state != _OKAY:
                    limit = index
                else:
                    break
            if limit is not None:
                self.__fh.truncate(limit * self.__record_size)
        self.__fh.flush()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
