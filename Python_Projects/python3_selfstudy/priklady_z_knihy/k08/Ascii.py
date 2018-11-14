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

import string


# Snadné, ale pomalé, protože musí vždy zkontrolovat zkontrolovat všechny:
#   is_ascii = lambda s: all(map(lambda c: ord(c) < 127, s))
# Těžší, ale rychlejší, protože pro zastavení stačí najít protipříklad
is_ascii = lambda s: not any(map(lambda c: ord(c) >= 127, s))
is_ascii.__doc__ = """\
    >>> is_ascii("Hlas lidu")
    True
    >>> is_ascii("Všeobecné hlasovací právo")
    False
    """

is_ascii_punctuation = (
        lambda s: not any(map(lambda c: c not in string.punctuation, s)))
is_ascii_punctuation.__doc__ = """\
    >>> is_ascii_punctuation("V žádném případě!")
    False
    >>> is_ascii_punctuation("@!?*")
    True
    """

is_ascii_printable = (
        lambda s: not any(map(lambda c: c not in string.printable, s)))
is_ascii_printable.__doc__ = """\
    >>> is_ascii_printable("Nikdy!")
    True
    >>> is_ascii_printable("@!?*\\t\\n")
    True
    >>> is_ascii_printable("@!?*\\t\\x05\\n")
    False
    >>> is_ascii_printable("V žádném případě!")
    False
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
