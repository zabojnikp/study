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
Zjednodušená verze vestavěné třídy property, na níž si ukážeme
možnou implementaci a způsob práce deskriptorů.

>>> contact = NameAndExtension("Joe", 135)
>>> contact.name, contact.extension
('Joe', 135)
>>> contact.X
Traceback (most recent call last):
    ...
AttributeError: 'NameAndExtension' object has no attribute 'X'
>>> contact.name = "Jane"
Traceback (most recent call last):
    ...
AttributeError: 'name' je pouze pro čtení
>>> contact.name
'Joe'
>>> contact.extension = 975
>>> contact.extension
975
"""

class Property:

    def __init__(self, getter, setter=None):
        self.__getter = getter
        self.__setter = setter
        self.__name__ = getter.__name__


    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.__getter(instance)


    def __set__(self, instance, value):
        if self.__setter is None:
            raise AttributeError("'{0}' je pouze pro čtení".format(
                                 self.__name__))
        return self.__setter(instance, value)


    def setter(self, setter):
        self.__setter = setter
        return self.__setter


class NameAndExtension:

    def __init__(self, name, extension):
        self.__name = name
        self.extension = extension


    @Property               # Používá vlastní deskriptor Property
    def name(self):
        return self.__name


    @Property               # Používá vlastní deskriptor Property
    def extension(self):
        return self.__extension


    @extension.setter       # Používá vlastní deskriptor Property
    def extension(self, extension):
        self.__extension = extension


if __name__ == "__main__":
    import doctest
    doctest.testmod()

