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

_file_type_magic_pairs = (
    ("BZip", bytes.fromhex("425A")),
    ("GZip", bytes.fromhex("1F8B")),
    ("Bajtkód Javy", bytes.fromhex("CAFEBABE")),
    ("Obrázek JPEG", bytes.fromhex("FFD8FFE0")),
    ("MIDI", b"MThd"),
    ("PDF", b"%PDF"),
    ("Obrázek PNG", b".PNG"),
    ("Obrázek PNG", b"\x89PNG"),
    ("PostScript", b"%!"),
    ("Obrázek TIFF", bytes.fromhex("49492A00")),
    ("Obrázek TIFF", bytes.fromhex("4D4D002A")),
    ("Spustitelný soubor Unix", b"\x7FELF"),
    ("Spustitelný soubor Unix", b".ELF"),
    ("Spustitelný soubor Windows", b"MZ"),
    ("Obrázek XPM", b"/* XPM */"),
    ("ZIP", bytes.fromhex("504B0304")),
    )


def get_file_type(text, extension):
    if extension.lower() in {".htm", ".html"}:
        return "HTML"
    if text.startswith(b"<?xml"):
        return "XML"
    if text[:2] == b"#!":
        text = text.lower()
        if b"python" in text:
            return "Python Program"
        elif b"perl" in text:
            return "Perl Program"
        else:
            return "Shell Script"
    for file_type, magic in _file_type_magic_pairs:
        if magic == text[:len(magic)]:
            return file_type
    
