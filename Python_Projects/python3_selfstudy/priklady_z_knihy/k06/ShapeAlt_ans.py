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
Tento modul poskytuje třídy Point a Circle.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math


class Point:

    def __init__(self, x=0, y=0):
        """2D kartézská souřadnice

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y


    @property
    def distance_from_origin(self):
        """Vrátí vzdálenost bodu od počátku

        >>> point = Point(3, 4)
        >>> point.distance_from_origin
        5.0
        """
        return math.hypot(self.x, self.y)


    def __add__(self, other):
        """Vrátí nový objekt typu Point, jehož souřadnice jsou součtem
        tohoto a druhého objektu

        >>> p = Point(2, 4)
        >>> q = p + Point(3, 5)
        >>> q
        Point(5, 9)
        """
        return Point(self.x + other.x, self.y + other.y)


    def __iadd__(self, other):
        """Vrátí tento objekt typu Point, jehož souřadnice jsou součtem
        tohoto a druhého objektu

        >>> p = Point(2, 4)
        >>> p += Point(3, 5)
        >>> p
        Point(5, 9)
        """
        self.x += other.x
        self.y += other.y
        return self


    def __sub__(self, other):
        """Vrátí nový objekt typu Point, jehož souřadnice jsou rozdílem
        tohoto a druhého objektu

        >>> p = Point(2, 4)
        >>> q = p - Point(3, 5)
        >>> q
        Point(-1, -1)
        """
        return Point(self.x - other.x, self.y - other.y)


    def __isub__(self, other):
        """Vrátí tento objekt typu Point, jehož souřadnice jsou rozdílem
        tohoto a druhého objektu

        >>> p = Point(2, 4)
        >>> p -= Point(3, 5)
        >>> p
        Point(-1, -1)
        """
        self.x -= other.x
        self.y -= other.y
        return self


    def __mul__(self, other):
        """Vrátí nový objekt typu Point, jehož souřadnice vznilky vynásobením 
        těchto souřadnic se souřadnicemi druhého objektu

        >>> p = Point(2, 4)
        >>> q = p * 3
        >>> q
        Point(6, 12)
        """
        return Point(self.x * other, self.y * other)


    def __imul__(self, other):
        """Vrátí tento objekt typu Point, jehož souřadnice jsou vynásobeny 
        se souřadnicemi druhého objektu

        >>> p = Point(2, 4)
        >>> p *= 3
        >>> p
        Point(6, 12)
        """
        self.x *= other
        self.y *= other
        return self


    def __truediv__(self, other):
        """Vrátí nový objekt typu Point, jehož souřadnice vznilky vydělením 
        těchto souřadnic souřadnicemi druhého objektu

        >>> p = Point(2, 4)
        >>> q = p / 2
        >>> q
        Point(1.0, 2.0)
        """
        return Point(self.x / other, self.y / other)


    def __itruediv__(self, other):
        """Vrátí tento objekt typu Point, jehož souřadnice jsou vyděleny 
        souřadnicemi druhého objektu

        >>> p = Point(2, 4)
        >>> p /= 2
        >>> p
        Point(1.0, 2.0)
        """
        self.x /= other
        self.y /= other
        return self


    def __floordiv__(self, other):
        """Vrátí nový objekt typu Point, jehož souřadnice vznilky celočíselným
        dělením se souřadnicemi druhého objektu

        >>> p = Point(2, 4)
        >>> q = p // 2
        >>> q
        Point(1, 2)
        """
        return Point(self.x // other, self.y // other)


    def __ifloordiv__(self, other):
        """Vrátí tento objekt typu Point, na jehož souřadnice aplikuje celočíselné
        dělení souřadnicemi druhého objektu

        >>> p = Point(2, 4)
        >>> p //= 2
        >>> p
        Point(1, 2)
        """
        self.x //= other
        self.y //= other
        return self


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return ("{0.__class__.__name__}({0.x!r}, {0.y!r})".format(
                self))


    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """Kruh

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius


    @property
    def area(self):
        """Plocha kruhu

        >>> circle = Circle(3)
        >>> a = circle.area
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)


    @property
    def edge_distance_from_origin(self):
        """Vzdálenost okraje kruhu od počátku

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin
        3.0
        """
        return abs(self.distance_from_origin - self.radius)


    @property
    def circumference(self):
        """Obvod kruhu

        >>> circle = Circle(3)
        >>> d = circle.circumference
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius


    @property
    def radius(self):
        """Poloměr kruhu

        >>> circle = Circle(-2)
        Traceback (most recent call last):
        ...
        AssertionError: poloměř musí být nenulový a nezáporný
        >>> circle = Circle(4)
        >>> circle.radius = -1
        Traceback (most recent call last):
        ...
        AssertionError: poloměř musí být nenulový a nezáporný
        >>> circle.radius = 6
        """
        return self.__radius

    @radius.setter
    def radius(self, radius):
        assert radius > 0, "poloměř musí být nenulový a nezáporný"
        self.__radius = radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        return ("{0.__class__.__name__}({0.radius!r}, {0.x!r}, "
                "{0.y!r})".format(self))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

