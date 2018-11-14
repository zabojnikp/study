#!/usr/bin/env python3

import random

#set values for the table
def get_int(msg, default, minimum_value):
    while True:
        try:
            user_input = input(msg)
            if not user_input and default is not None:
                return default

            elif int(user_input) < minimum_value:
                print('Values has to be >=', minimum_value)
            
            else:
                return int(user_input)
        
        except ValueError as err:
            print(err)

def evaluate_maximum(minimum_value):
    ''' Evaluates maximum in case user inputs minimum value >  default value for maximum'''

    value = get_int('Set maximum value or Enter for 1000: ', 1000, minimum_value)
    if value < minimum_value:
        return minimum_value * 2
    else:
        return value

rows = get_int('Set number for rows: ', None, 1)
columns = get_int('Set number for columns: ', None, 1)
minimum = get_int('Set minimum value or Enter for 0: ', 0, -1000000)
maximum = evaluate_maximum(minimum)

#print a table
row = 0
while row < rows:
    column = 0
    line = ''
    while column < columns:
        number = random.randint(minimum, maximum)
        s = str(number)
        line += s + " "
        column += 1
    row += 1
    print(line)