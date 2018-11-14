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

import html.entities
import os
import re
import sys


def main():
    if len(sys.argv) > 1 and sys.argv[1] in {"-h", "--help"}:
        print("""použití: {0} [vstupní_soubor] [výstupní_soubor]
nejsou-li uvedeny žádné soubory, pak čte ze standardního vstupu
a zapisuje na standardní výstup;
je-li uveden jeden soubor, pak čte z tohoto souboru 
a zapisuje na standardní výstup;
jsou-li uvedeny oba soubory, pak čte první a zapisuje do druhého
""".format(os.path.basename(sys.argv[0])))
        sys.exit(2)

    fin, fout = (sys.stdin, sys.stdout)
    close_in, close_out = (False, False)
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], encoding="utf8")
        close_in = True
        if len(sys.argv) > 2:
            fout = open(sys.argv[2], "w", encoding="utf8")
            close_out = True
    html_text = fin.read()
    if close_in:
        fin.close()
    fout.write(html2text(html_text))
    if close_out:
        fout.close()
    else:
        print()


def html2text(html_text):
    def char_from_entity(match):
        code = html.entities.name2codepoint.get(match.group(1), 0xFFFD)
        return chr(code)

    text = re.sub(r"<!--(?:.|\n)*?-->", "", html_text)          #1
    text = re.sub(r"<[Pp][^>]*?>", "\n\n", text)                #2
    text = re.sub(r"<[^>]*?>", "", text)                        #3
    text = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), text)
    text = re.sub(r"&([A-Za-z]+);", char_from_entity, text)     #5 
    text = re.sub(r"\n(?:[ \xA0\t]+\n)+", "\n", text)           #6
    return re.sub(r"\n\n+", "\n\n", text.strip())               #7


main()
