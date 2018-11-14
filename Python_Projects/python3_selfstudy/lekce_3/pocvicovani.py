import collections

#vytvoreni nove datove tridy(typu) Sale, pomoci niz muzeme vytvaret pojmenovane n-tice
#prvni argument je nazev datove tridy(typu) n-tice
#druhy argument je nazev jednolivych prvku n-tice  
Sale = collections.namedtuple('Sale', 'product_id customer_id date quantity price')

sales = []
sales.append(Sale(432, 921, '2008-09-14', 3, 79.9))
sales.append(Sale(419, 874, '2008-09-15', 1, 184.9))
print(sales)

total = 0
for Sale in sales:
    total += Sale.quantity * Sale.price

print('celkem {0:.2f} Kc'.format(total))

Aircraft = collections.namedtuple('Aircraft', 'manufacturer model seating')
Seating = collections.namedtuple('Seating', 'minimum maximum')
aircraft = Aircraft('Airbus', 'A320-200', Seating(100, 200))
print(aircraft.seating.maximum)
print('{0}, {1}'.format(aircraft.manufacturer, aircraft.model))
print('{manufacturer}, {model}'.format(**aircraft._asdict()))

#starred arguments
first, *mid, last = "Karel Filip Artur Jiri Podebrad".split()
print(first)
print(mid)
print(last)

def product (a, b, c):
    return a * b * c

L = [2, 3, 5]

print(product(*L))
print(product(2, *L[1:]))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x[1::2] = [0] * len(x[1::2])
print(x)

#list komprehenze
leap = []
for year in range (2000, 2050):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap.append(year)
print(leap)

leap = [year for year in range(2000, 2050) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
print(leap)

#mnoziny
# add s
first = set('pecan')
second = set('pie')
first.add('s')
print(first)
#return from first set only those which are not in second set
print(first - second)
print(first.difference(second))
#delete s
first.discard('s')
print(first)
#return same data from both sets
print(first & second)
print(first.intersection(second))
#verify there is no data same
print(first.isdisjoint(second))
#return unique data
print(first ^ second)
print(first.symmetric_difference(second))
#return new subset with all data
print(first | second)
print(first.union(second))