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
Tento modul nabízí třídu Image, která uchovává trojice (x, y, barva)
a barvu pozadí poskytující jistý druh reprezentace obrázku pomocí řídkého 
pole. K dispozici je též metoda pro export obrázku do formátu XPM.

>>> import os
>>> import tempfile
>>> red = "#FF0000"
>>> blue = "#0000FF"
>>> img = os.path.join(tempfile.gettempdir(), "test.img")
>>> xpm = os.path.join(tempfile.gettempdir(), "test.xpm")
>>> image = Image(10, 8, img)
>>> for x, y in ((0, 0), (0, 7), (1, 0), (1, 1), (1, 6), (1, 7), (2, 1),
...             (2, 2), (2, 5), (2, 6), (2, 7), (3, 2), (3, 3), (3, 4),
...             (3, 5), (3, 6), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4),
...             (5, 5), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 1),
...             (7, 2), (7, 5), (7, 6), (7, 7), (8, 0), (8, 1), (8, 6),
...             (8, 7), (9, 0), (9, 7)):
...    image[x, y] = blue
>>> for x, y in ((3, 1), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2),
...             (6, 1)):
...    image[(x, y)] = red
>>> print(image.width, image.height, len(image.colors), image.background)
10 8 3 #FFFFFF
>>> border_color = "#FF0000" # red
>>> square_color = "#0000FF" # blue
>>> width, height = 240, 60
>>> midx, midy = width // 2, height // 2
>>> image = Image(width, height, img, "#F0F0F0")
>>> for x in range(width):
...     for y in range(height):
...         if x < 5 or x >= width - 5 or y < 5 or y >= height -5:
...             image[x, y] = border_color
...         elif midx - 20 < x < midx + 20 and midy - 20 < y < midy + 20:
...             image[x, y] = square_color
>>> print(image.width, image.height, len(image.colors), image.background)
240 60 3 #F0F0F0
>>> image.save()
>>> newimage = Image(1, 1, img)
>>> newimage.load()
>>> print(newimage.width, newimage.height, len(newimage.colors), newimage.background)
240 60 3 #F0F0F0
>>> image.export(xpm)
>>> image.thing
Traceback (most recent call last):
...
AttributeError: 'Image' object has no attribute 'thing'
>>> for name in (img, xpm):
...     try:
...         os.remove(name)
...     except EnvironmentError:
...         pass
"""

import os
import pickle

USE_GETATTR = False


class ImageError(Exception): pass
class CoordinateError(ImageError): pass
class LoadError(ImageError): pass
class SaveError(ImageError): pass
class ExportError(ImageError): pass
class NoFilenameError(ImageError): pass


class Image:

    def __init__(self, width, height, filename="",
                 background="#FFFFFF"):
        """Obrázek reprezentovaný jako hodnoty barev ve stylu HTML
        (názvy barev nebo řetězce s šestnáctkovými číslicemi) na souřadnicích (x, y) 
        s tím, že vynechané body jsou považovány za pozadí.
        """
        self.filename = filename
        self.__background = background
        self.__data = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}


    if USE_GETATTR:
        def __getattr__(self, name):
            """
            >>> image = Image(10, 10)
            >>> len(image.colors) == 1
            True
            >>> image.width == image.height == 10
            True
            >>> image.thing
            Traceback (most recent call last):
            ...
            AttributeError: 'Image' object has no attribute 'thing'
            """
            if name == "colors":
                return set(self.__colors)
            classname = self.__class__.__name__
            if name in frozenset({"background", "width", "height"}):
                return self.__dict__["_{classname}__{name}".format(
                        **locals())]
            raise AttributeError("'{classname}' object has no "
                    "attribute '{name}'".format(**locals()))
    else:
        @property
        def background(self):
            return self.__background


        @property
        def width(self):
            return self.__width


        @property
        def height(self):
            return self.__height


        @property
        def colors(self):
            return set(self.__colors)


    def __getitem__(self, coordinate):
        """Vrátí barvu na zadané souřadnici (x, y), což bude
        barva pozadí, pokud v tomto bodě nebyla nastavena
        """
        assert len(coordinate) == 2, "souřadnice musí být n-tice se dvěma prvky"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        return self.__data.get(tuple(coordinate), self.__background)


    def __setitem__(self, coordinate, color):
        """Nastaví barvu na zadané souřadnici (x, y)
        """
        assert len(coordinate) == 2, "souřadnice musí být n-tice se dvěma prvky"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        if color == self.__background:
            self.__data.pop(tuple(coordinate), None)
        else:
            self.__data[tuple(coordinate)] = color
            self.__colors.add(color)


    def __delitem__(self, coordinate):
        """Vymaže barvu na zadané souřadnici (x, y)

        Tím se v podstatě změní barva v tomto bodě na barvu pozadí.
        """
        assert len(coordinate) == 2, "souřadnice musí být n-tice se dvěma prvky"
        if (not (0 <= coordinate[0] < self.width) or
            not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        self.__data.pop(tuple(coordinate), None)


    def save(self, filename=None):
        """Uloží aktuální obrázek

        Pokud je parametr filename zadán, uloží se do interního atributu
        a použije pro načtení.
        """
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None
        try:
            data = [self.width, self.height, self.__background,
                    self.__data]
            fh = open(self.filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

        
    def load(self, filename=None):
        """Načte aktuální obrázek

        Pokud je parametr filename zadán, uloží se do interního atributu 
        a použije pro načtení.
        """
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None
        try:
            fh = open(self.filename, "rb")
            data = pickle.load(fh)
            (self.__width, self.__height, self.__background,
             self.__data) = data
            self.__colors = (set(self.__data.values()) |
                             {self.__background})
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()


    def export(self, filename):
        """Exportuje obrázek do zadaného souboru
        """
        if filename.lower().endswith(".xpm"):
            self.__export_xpm(filename)
        else:
            raise ExportError("nepodporovaný formnát pro export: " +
                              os.path.splitext(filename)[1])


    def __export_xpm(self, filename):
        """Exportuje obrázek jako soubor XPM, pokud používá méně než 
        8930 barev
        """
        name = os.path.splitext(os.path.basename(filename))[0]
        count = len(self.__colors)
        chars = [chr(x) for x in range(32, 127) if chr(x) != '"']
        if count > len(chars):
            chars = []
            for x in range(32, 127):
                if chr(x) == '"':
                    continue
                for y in range(32, 127):
                    if chr(y) == '"':
                        continue
                    chars.append(chr(x) + chr(y))
        chars.reverse()
        if count > len(chars):
            raise ExportError("nemohu exportovat do souboru XPM: příliš mnoho barev")
        fh = None
        try:
            fh = open(filename, "w", encoding="ascii")
            fh.write("/* XPM */\n")
            fh.write("static char *{0}[] = {{\n".format(name))
            fh.write("/* columns rows colors chars-per-pixel */\n")
            fh.write('"{0.width} {0.height} {1} {2}",\n'.format(
                     self, count, len(chars[0])))
            char_for_colour = {}
            for color in self.__colors:
                char = chars.pop()
                fh.write('"{char} c {color}",\n'.format(**locals()))
                char_for_colour[color] = char
            fh.write("/* pixels */\n")
            for y in range(self.height):
                row = []
                for x in range(self.width):
                    color = self.__data.get((x, y), self.__background)
                    row.append(char_for_colour[color])
                fh.write('"{0}",\n'.format("".join(row)))
            fh.write("};\n")
        except EnvironmentError as err:
            raise ExportError(str(err))
        finally:
            if fh is not None:
                fh.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
