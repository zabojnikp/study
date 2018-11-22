#!/usr/bin/env python3

class FuzzyBool(float):
    def __new__(cls, value=0.0):
        return super().__new__(cls, value if 0.0 <= value <= 1.0 else 0.0)

    def __invert__(self):
       return (1.0 - float(self))

    def __and__(self, other):
        return min(self, other)   
    
    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, super().__repr__()))

    def __bool__(self):
        return self > 0.5

    def __int__(self):
        return round(self)

    def __add__(self, other):
        raise NotImplementedError()   

    def __eq__(self, other):
        return NotImplemented 
    
    for name, operator in (("__neg__", "-"), ("__index__", "index()")):
        message = ("bad operand for unary {0}: '{{self}}'".format(operator))
        exec("def {0}(self): raise TypeError(\"{1}\".format("
             "self=self.__class__.__name__))".format(name, message))

intance1 = FuzzyBool(.5)
print(intance1)
#print(-intance1)