def get_integer(msg):
    try:
        user_input = input(msg)
        value = int(user_input)
    except ValueError as err:
        print(err)
    return value

nasobky = []
divisor = get_integer("divisor: ")
start = get_integer("start: ")
stop = get_integer("stop: ")

if divisor != 0:
    index = stop // divisor
    if start >= divisor:
        for i in range(start, stop + 1, divisor):
            nasobky.append(i)
    else:
        for i in range(divisor, stop + 1, divisor):
            nasobky.append(i)

    print(nasobky)

else:
    print("Cannot divide by zero")