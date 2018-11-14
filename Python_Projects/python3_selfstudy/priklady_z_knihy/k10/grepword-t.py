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
import queue
import threading


# maximální délka hledaného slova je BLOCK_SIZE
BLOCK_SIZE = 8000


class Worker(threading.Thread):

    def __init__(self, work_queue, word, number):
        super().__init__()
        self.work_queue = work_queue
        self.word = word
        self.number = number


    def run(self):
        while True:
            try:
                filename = self.work_queue.get()
                self.process(filename)
            finally:
                self.work_queue.task_done()


    def process(self, filename):
        previous = ""
        try:
            with open(filename, "rb") as fh:
                while True:
                    current = fh.read(BLOCK_SIZE)
                    if not current:
                        break
                    current = current.decode("utf8", "ignore")
                    if (self.word in current or
                        self.word in previous[-len(self.word):] +
                                     current[:len(self.word)]):
                        print("{0}{1}".format(self.number, filename))
                        break
                    if len(current) != BLOCK_SIZE:
                        break
                    previous = current
        except EnvironmentError as err:
            print("{0}{1}".format(self.number, err))


def main():
    opts, word, args = parse_options()
    filelist = get_files(args, opts.recurse)
    work_queue = queue.Queue()
    for i in range(opts.count):
        number = "{0}: ".format(i + 1) if opts.debug else ""
        worker = Worker(work_queue, word, number)
        worker.daemon = True
        worker.start()
    for filename in filelist:
        work_queue.put(filename)
    work_queue.join()


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
