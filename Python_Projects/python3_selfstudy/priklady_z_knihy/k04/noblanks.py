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
Načte textové soubory a zapíše odpovídající soubory .nb bez prázdných 
řádků.
"""

import os
import sys


def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines


def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        for line in lines:
            fh.write(line)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()


if len(sys.argv) < 2:
    print("použití: noblanks.py soubor1 [soubor2 [... souborN]]")
    sys.exit()

for filename in sys.argv[1:]:
    lines = read_data(filename)
    if lines:
        write_data(lines, os.path.splitext(filename)[0] + ".nb")

