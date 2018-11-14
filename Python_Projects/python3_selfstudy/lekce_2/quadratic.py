import sys, math, cmath

def get_float(msg, allow_zero):
    '''THIS IS TO GET FLOAT NUMBER, AND VERIFY IF OK'''
    user_input = None
    while user_input is None:
        try:
            user_input = float(input(msg))
            if not allow_zero and abs(user_input) < sys.float_info.epsilon:
                print('Cannot use 0 for this constant')
                user_input = None
        except ValueError as err:
            print(err)
    return user_input

a = get_float('input a: ', False)
b = get_float('input b: ', True)
c = get_float('input c: ', True)

#print("{}x\N{SUPERSCRIPT TWO} {:+} x {:+} = 0".format(a, b, c))

x1 = None
x2 = None
diskriminant = (b ** 2) - (4 * a * c)
if diskriminant == 0:
    x1 = -(b / (2 * a))
else:
    if diskriminant > 0:
        root = math.sqrt(diskriminant)
    else:
        root = cmath.sqrt(diskriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

#vypis rovnice bez 0.0
equation = "{0}x\N{SUPERSCRIPT TWO} ".format(a)
if b != 0:
    if b > sys.float_info.epsilon:
        equation += "+ {0}x ".format(abs(b))
    else:
        equation += "- {0}x ".format(abs(b))

if c != 0:
    if c > sys.float_info.epsilon:
        equation += "+ {0} ".format(abs(c))
    else:
        equation += "- {0} ".format(abs(c))

equation += "= 0 \N{RIGHTWARDS ARROW} x = {x1:.3f}".format(**locals())

if x2 is not None:
    equation += " or x = {x2:.3f}".format(**locals())

print(equation)