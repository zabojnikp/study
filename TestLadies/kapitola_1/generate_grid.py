import random

def get_int(msg, minimum, default):
    while True:
        try:
            user_input = input(msg)

            if not user_input and default is not None:
                return default
            

            elif int(user_input) < minimum:
                print("Value needs to be >= ", minimum)
            
            else:
                return int(user_input)

        except ValueError as err:
            print(err)

def evaluate_maximum(min):
    value = get_int('Set maximum value or Enter for 1000: ', min, 1000)
    if value < min:
        return min * 2
    else:
        return value

rows = get_int("Input rows: ", 1, None)
columns = get_int('Input columns: ', 1, None)
minimum_value = get_int("Set minimum value or Enter for 0:", -100000000, 0)
maximum_value = evaluate_maximum(minimum_value)

row = 0
while row < rows:
    column = 0
    line = ''
    while column < columns:
        value = random.randint(minimum_value, maximum_value)
        grid_value = str(value)
        while len(grid_value) < 10:
            grid_value = " " + grid_value
        line += grid_value
        column += 1
    print(line)
    row += 1


