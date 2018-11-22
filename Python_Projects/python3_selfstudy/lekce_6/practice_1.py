class MyDict(dict): pass
d = MyDict.fromkeys("VEINS", 3)
print(str(d))

#vraci seznam
def letter_range_1(a, z):
    result = []
    while ord(a) < ord(z):
        result.append(a)
        a = chr(ord(a) + 1)
    return result

print(letter_range_1("m", "v"))

#vraci generator
def letter_range_2(a, z):
    while ord(a) < ord(z):
        yield a
        a = chr(ord(a) + 1)

print(list(letter_range_2("m", 'v')))