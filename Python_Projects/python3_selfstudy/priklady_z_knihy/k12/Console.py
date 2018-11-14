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

import sys


class _RangeError(Exception): pass


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80,
               force_lower=False):
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
                    raise ValueError("{0} may not be empty".format(
                                     name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{0} musí mít nejméně {1} a "
                        "nejvíce {2} znaků".format(
                        name, minimum_length, maximum_length))
            return line if not force_lower else line.lower()
        except ValueError as err:
            print("CHYBA", err)


def get_integer(message, name="integer", default=None, minimum=None,
                maximum=None, allow_zero=True):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            x = int(line)
            if x == 0:
                if allow_zero:
                    return x
                else:
                    raise _RangeError("{0} nesmí být 0".format(name))
            if ((minimum is not None and minimum > x) or 
                (maximum is not None and maximum < x)):
                raise _RangeError("{0} musí být mezi {1} a {2} "
                        "včetně {3}".format(name, minimum, maximum,
                        (" (nebo 0)" if allow_zero else "")))
            return x
        except _RangeError as err:
            print("CHYBA", err)
        except ValueError as err:
            print("CHYBA {0} musí být celé číslo".format(name))


def get_float(message, name="float", default=None, minimum=None,
              maximum=None, allow_zero=True):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            x = float(line)
            if abs(x) < sys.float_info.epsilon:
                if allow_zero:
                    return x
                else:
                    raise _RangeError("{0} nesmí být 0.0".format(
                                      name))
            if ((minimum is not None and minimum > x) or 
                (maximum is not None and maximum < x)):
                raise _RangeError("{0} musí být mezi {1} a {2} "
                        "včetně {3}".format(name, minimum, maximum,
                        (" (nebo 0.0)" if allow_zero else "")))
            return x
        except _RangeError as err:
            print("CHYBA", err)
        except ValueError as err:
            print("ERROR {0} must be a float".format(name))


def get_bool(message, default=None):
    yes = frozenset({"1", "a", "ano", "t", "true", "ok"})
    message += " (a/ano/n/ne)"
    message += ": " if default is None else " [{0}]: ".format(default)
    line = input(message)
    if not line and default is not None:
        return default in yes
    return line.lower() in yes


def get_date(message, default=None, format="%y-%m-%d"):
    # parametr message by měl obsahovat formát v podobě čitelné pro člověka,
    # např %y-%m-%d, "YY-MM-DD".
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            return datetime.datetime.strptime(line, format)
        except ValueError as err:
            print("CHYBA", err)


def get_menu_choice(message, valid, default=None, force_lower=False):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        line = input(message)
        if not line and default is not None:
            return default
        if line not in valid:
            print("CHYBA pouze {0} jsou platné volby".format(
                  ", ".join(["'{0}'".format(x)
                  for x in sorted(valid)])))
        else:
            return line if not force_lower else line.lower()

