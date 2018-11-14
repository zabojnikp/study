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

import optparse
import os
import subprocess
import sys


def main():
    child = os.path.join(os.path.dirname(__file__),
                         "grepword-p-child.py")
    opts, word, args = parse_options()
    filelist = get_files(args, opts.recurse)
    files_per_process = len(filelist) // opts.count
    start, end = 0, files_per_process + (len(filelist) % opts.count)
    number = 1

    pipes = []
    while start < len(filelist):
        command = [sys.executable, child]
        if opts.debug:
            command.append(str(number))
        pipe = subprocess.Popen(command, stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        pipes.append((pipe, pipe.stdout))
        pipe.stdin.write(word.encode("utf8") + b"\n")
        for filename in filelist[start:end]:
            pipe.stdin.write(filename.encode("utf8") + b"\n")
        pipe.stdin.close()
        number += 1
        start, end = end, end + files_per_process

    results = []
    while pipes:
        pipe, stdout = pipes.pop()
        results.extend(stdout.readlines())
        pipe.wait()
    for line in sorted(results):
        print(line.decode("utf8").rstrip())


def parse_options():
    parser = optparse.OptionParser(
            usage=("použití: %prog [volby] slovo název1 "
                   "[název2 [... názevN]]\n\n"
                   "názvy jsou názvy souborů nebo cesty; samotné cesty "
                   "mají smysl s volbou -r"))
    parser.add_option("-p", "--processes", dest="count", default=7,
            type="int",
            help=("kolik podřízených procesů se má použít (1..20) "
                  "[výchozí %default]"))
    parser.add_option("-r", "--recurse", dest="recurse",
            default=False, action="store_true",
            help="rekurzivní sestup do podadresářů")
    parser.add_option("-d", "--debug", dest="debug", default=False,
                      action="store_true")
    opts, args = parser.parse_args()
    if len(args) == 0:
        parser.error("musí být zadáno slovo a alepoň jedna cesta")
    elif len(args) == 1:
        parser.error("musí být zadána alepoň jedna cesta")
    if (not opts.recurse and
        not any([os.path.isfile(arg) for arg in args])):
        parser.error("musí být zadán alepoň jeden soubor; nebo použijte volbu -r")
    if not (1 <= opts.count <= 20):
        parser.error("počet procesů musí být mezi 1..20")
    return opts, args[0], args[1:]


def get_files(args, recurse):
    filelist = []
    for path in args:
        if os.path.isfile(path):
            filelist.append(path)
        elif recurse:
            for root, dirs, files in os.walk(path):
                for filename in files:
                    filelist.append(os.path.join(root, filename))
    return filelist

    
main()
