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


Language = "cs"

ENGLISH = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
           5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
CZECH = {0: "nula", 1: "jedna", 2: "dvě", 3: "tři", 4: "čtyři",
         5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"}


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("použití: {0} [en|cs] číslo".format(sys.argv[0]))
        sys.exit()

    args = sys.argv[1:]
    if args[0] in {"en", "cs"}:
        global Language
        Language = args.pop(0)
    print_digits(args.pop(0))


def print_digits(digits):
    dictionary = ENGLISH if Language == "en" else CZECH
    for digit in digits:
        print(dictionary[int(digit)], end=" ")
    print()


main()
