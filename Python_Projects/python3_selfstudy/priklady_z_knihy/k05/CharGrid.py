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
This module provides functionality for writing characters on a grid.

The module provides functions for adding horizontal and vertical lines,
and for (optionally filled) rectangles, and for (optionally boxed) text.

All char arguments must be strings of length 1; these are guarded by
assertions. If out of range row or column values are given, the
appropriate exception, RowRangeError or ColumnRangeError will
be raised---use the RangeError exception if you want to catch either.

>>> resize(14, 50)
>>> add_rectangle(0, 0, *get_size())
>>> add_vertical_line(5, 10, 13)
>>> add_vertical_line(2, 9, 12, "!")
>>> add_horizontal_line(3, 10, 20, "+")
>>> add_rectangle(0, 0, 5, 5, "%")
>>> add_rectangle(5, 7, 12, 40, "#", True)
>>> add_rectangle(7, 9, 10, 38, " ")
>>> add_text(8, 10, "Tohle je náš modul CharGrid")
>>> add_text(1, 32, "Pěkně odporný", "@")
>>> add_rectangle(6, 42, 11, 46, fill=True)
>>> render(False)
%%%%%*********************************************
%   %                           @@@@@@@@@@@@@@@  *
%   %                           @Pěkně odporný@  *
%   %     ++++++++++            @@@@@@@@@@@@@@@  *
%%%%%                                            *
*      #################################         *
*      #################################  ****   *
*      ##                             ##  ****   *
*      ## Tohle je náš modul CharGrid ##  ****   *
* !    ##                             ##  ****   *
* !  | #################################  ****   *
* !  | #################################         *
*    |                                           *
**************************************************
"""

import subprocess
import sys


class RangeError(Exception): pass
class RowRangeError(RangeError): pass
class ColumnRangeError(RangeError): pass


_CHAR_ASSERT_TEMPLATE = ("je nutné zadat jediný znak: '{0}' "
                         "je příliš dlouhý")
_max_rows = 25
_max_columns = 80
_grid = []
_background_char = " "


if sys.platform.startswith("win"): 
    def clear_screen():
        subprocess.call(["cmd.exe", "/C", "cls"])
else:
    def clear_screen():
        subprocess.call(["clear"])
clear_screen.__doc__ = """Vymaže obrazovku pomocí příkazu pro \
vymazání obrazovky aktuálně používaného systému"""


def char_at(row, column):
    """Vrátí znak na zadané pozici

    Používá se pouze pro účely ladění.

    >>> char_at(0, 0)
    '%'
    >>> char_at(4, 11)
    ' '
    >>> char_at(32, 24)
    Traceback (most recent call last):
    ...
    RowRangeError
    """
    try:
        return _grid[row][column]
    except IndexError:
        if not 0 <= row <= _max_rows:
            raise RowRangeError()
        raise ColumnRangeError()


def set_background(char=" "):
    """Nastaví znak pro pozadí

    >>> set_background("$")
    >>> char_at(0, 0)
    '%'
    >>> char_at(4, 24)
    '$'
    >>> set_background("<>")
    Traceback (most recent call last):
    ...
    AssertionError: je nutné zadat jediný znak: '<>' je příliš dlouhý
    >>> set_background(" ")
    """
    assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
    global _background_char
    old_background_char = _background_char
    _background_char = char
    for row in range(_max_rows):
        for column in range(_max_columns):
            if _grid[row][column] == old_background_char:
                _grid[row][column] = _background_char


def add_vertical_line(column, row0, row1, char="|"):
    """Přidá do mřížky svislou čáru s použitím zadaného znaku

    >>> add_vertical_line(5, 2, 10, "&")
    >>> char_at(2, 5) == char_at(3, 5) == "&"
    True
    >>> add_vertical_line(85, 1, 2)
    Traceback (most recent call last):
    ...
    ColumnRangeError
    """
    assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
    try:
        for row in range(row0, row1):
            _grid[row][column] = char
    except IndexError:
        if not 0 <= row <= _max_rows:
            raise RowRangeError()
        raise ColumnRangeError()
    

def add_horizontal_line(row, column0, column1, char="-"):
    """Přidá do mřížky vodorovnou čáru s použití zadaného znaku

    >>> add_horizontal_line(8, 20, 25, "=")
    >>> char_at(8, 20) == char_at(8, 24) == "="
    True
    >>> add_horizontal_line(31, 11, 12)
    Traceback (most recent call last):
    ...
    RowRangeError
    """
    assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
    try:
        for column in range(column0, column1):
            _grid[row][column] = char
    except IndexError:
        if not 0 <= row <= _max_rows:
            raise RowRangeError()
        raise ColumnRangeError()
    

def add_rectangle(row0, column0, row1, column1, char="*", fill=False):
    """Přidá do mřížky obdélník s použitím zadaného znaku pro
    obrys
    
    Je-li filled true, vyplní obdélník zadaným znakem.

    >>> add_rectangle(10, 30, 14, 35, "^", True)
    >>> char_at(10, 30) == char_at(12, 32) == "^"
    True
    >>> add_rectangle(10, 30, 14, 35, "!")
    >>> char_at(10, 30) == char_at(13, 34) == "!"
    True
    >>> add_rectangle(10, 30, 14, 95, "x")
    Traceback (most recent call last):
    ...
    ColumnRangeError
    >>> add_rectangle(10, 30, 14, 95)
    Traceback (most recent call last):
    ...
    ColumnRangeError
    """
    if not fill:
        add_vertical_line(column0, row0, row1, char)
        add_vertical_line(column1 - 1, row0, row1, char)
        add_horizontal_line(row0, column0, column1, char)
        add_horizontal_line(row1 - 1, column0, column1, char)
    else:
        assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
        try:
            for row in range(row0, row1):
                for column in range(column0, column1):
                    _grid[row][column] = char
        except IndexError:
            if not 0 <= row <= _max_rows:
                raise RowRangeError()
            raise ColumnRangeError()


def add_text(row, column, text, char=None):
    """Přidá do mřížky řetězec text 
    
    Pokud char není None, nakreslí kolem textu rámeček
    se zadaným znakem. Levý horní roh rámečku je jeden řádek nad
    a jeden sloupec vlevo od zadaného řádku a sloupce a rozprostírá se
    tak, aby obklopil celý text.

    >>> add_text(6, 15, "Alpha Beta")
    >>> char_at(6, 15) == "A"
    True
    >>> char_at(6, 19) == char_at(6, 24) == "a"
    True
    >>> add_text(11, 22, "Gamma", ":")
    >>> char_at(12, 23) == "G"
    True
    >>> char_at(12, 24) == char_at(12, 27) == "a"
    True
    >>> char_at(11, 24) == char_at(13, 27) == ":"
    True
    >>> add_text(10, 89, "Delta")
    Traceback (most recent call last):
    ...
    ColumnRangeError
    >>> add_text(110, 8, "Epsison", "O")
    Traceback (most recent call last):
    ...
    RowRangeError
    """
    try:
        if char is None:
            for i, column in enumerate(range(column,
                                             column + len(text))):
                _grid[row][column] = text[i]
        else:
            assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
            row0 = row
            row1 = row0 + 3
            column0 = column
            column1 = column0 + len(text) + 2
            add_rectangle(row0, column0, row1, column1, char)
            row = row0 + 1
            for i, column in enumerate(range(column0 + 1,
                                             column1 - 1)):
                _grid[row][column] = text[i]
    except IndexError:
        if not 0 <= row <= _max_rows:
            raise RowRangeError()
        raise ColumnRangeError()


def render(clear=True):
    """Vykreslí mřížku do konzole a vymaže ji
    """
    if clear:
        clear_screen()
    for row in range(_max_rows):
        print("".join(_grid[row]))
        for column in range(_max_columns):
            _grid[row][column] == _background_char


def get_size():
    """Vrátí velikost mřížky

    >>> get_size()
    (14, 50)
    """
    return _max_rows, _max_columns


def resize(max_rows, max_columns, char=None):
    """Změní velikost mřížky, přičemž zahodí obsah a 
    změní pozadí, nemá-li znak představující pozadí hodnotu None
    """
    assert max_rows > 0 and max_columns > 0, "příliš malé"
    global _grid, _max_rows, _max_columns, _background_char
    if char is not None:
        assert len(char) == 1, _CHAR_ASSERT_TEMPLATE.format(char)
        _background_char = char
    _max_rows = max_rows
    _max_columns = max_columns
    _grid = [[_background_char for column in range(_max_columns)]
             for row in range(_max_rows)]

    
resize(_max_rows, _max_columns)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

