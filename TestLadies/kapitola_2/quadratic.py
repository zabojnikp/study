import sys
import math
import cmath

def get_float(msg, allow_zero):
    while True:
        try:
            user_input = float(input(msg))
            if abs(user_input) < sys.float_info.epsilon and allow_zero == False:
                print("Not possible to use 0 for this. Try again.")
            
            else:
                number = float(user_input)
                return number

        except ValueError as err:
            print(err)

koef_a = get_float('Input a:', False)
koef_b = get_float('Input b: ', True)
koef_c = get_float('Input c: ', True)

diskriminant = (koef_b ** 2) - (4 * koef_a * koef_c)
x_1 = None
x_2 = None

if diskriminant == 0:
    x_1 = - (koef_b / (2 * koef_a))

else:
    if diskriminant > 0:
        root = math.sqrt(diskriminant)

    else:
        root = cmath.sqrt(diskriminant)

    x1 = (- koef_b + root) / (2 * koef_a)
    x2 = (- koef_b - root) / (2 * koef_a)


equation = ("{}x\N{SUPERSCRIPT TWO} + {}x + {} = 0 \N{RIGHTWARDS ARROW} x = {}").format(koef_a, koef_b, koef_c, x1)

if x2 is not None:
    equation += " or x = {x2}".format(**locals())

print(equation)

