#!/usr/bin/env python3
"""
Implementuje neměnitelný datový typ FuzzyBool, který může mít pouze hodnoty
z intervalu [0.0, 1.0], a který podporuje základní logické operace negace
(~), konfunkce (&) a disjunkce (|) s použitím fuzzy logiky.

>>> f = FuzzyBool()
>>> g = FuzzyBool(.5)
>>> h = FuzzyBool(3.75)
>>> f, g, h
(FuzzyBool(0.0), FuzzyBool(0.5), FuzzyBool(0.0))
>>> h = ~h
>>> print(f, g, h)
0.0 0.5 1.0
>>> f = FuzzyBool(0.2)
>>> f < g
True

>>> f + g
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +: 'FuzzyBool' and 'FuzzyBool'
>>> int(h), int(g)
(1, 0)
>>> d = {f : 1, g : 2, h : 3}
>>> d[g]
2
"""
class FuzzyBool:
    def __init__(self, value=0.0):
        self.__value = value if 0.0 <= value <= 1.0 else 0.0

    def __invert__(self):
        return (1.0 - self.__value)

    def __and__(self, other):
        return min(self.__value, other.__value)

    def __or__(self, other):
        return max(self.__value, other.__value)
    
    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, self.__value))
    
    def __str__(self):
        return str(self.__value)

    def __bool__(self):
        return self.__value > 0.5

    def __int__(self):
        return round(self.__value)

    def __float__(self):
        return float(self.__value)
    
    def __lt__(self, other):
        return self.__value < other.__value

    def __le__(self, other):
        return self.__value <= other.__value

    def __eq__(self, other):
        return self.__value == other.__value
    
    def __hash__(self):
        return hash(id(self))

    def __format__(self, format_spec):
        return format(self.__value, format_spec)

    def print_me(self, other):
        print("original_value:{0}, new_value:{1}".format(self.__value, other.__value))

    def conjuction(self, *fizzies):
        return min(fizzies)
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        assert 0.0 <= value <= 1.0, "může mít pouze hodnoty z intervalu [0.0, 1.0]"
        self.__value = value


if __name__ == "__main__":
    import doctest
    doctest.testmod()

value = FuzzyBool(1)
new_value = FuzzyBool(0.15)
value.print_me(new_value)
print(~value)
print(value & new_value)
print(value | new_value)
print(repr(value))
print(str(value))
print(bool(value))
print(bool(new_value))
print(int(value))
print(float(value))
#print(sum(value, new_value))
print(value == new_value)
print(value >= new_value)
print(hash(value))
f = FuzzyBool(.875)
g = FuzzyBool(.55)
print("{0:.1%} {1:.1%}".format(value, new_value))
print(f.conjuction(FuzzyBool(0.8), FuzzyBool(0.5), FuzzyBool(0.4)))


value.value = 0.7
print(value)