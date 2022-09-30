from ast import IsNot


def function_factorial(x):
    if x == 0:
        return 1
    if x == 1:
        return 1

    y = x - 1
    while y > 1:
        factorial = x * y
        y -= 1
        x = factorial
    return factorial


def function_NcR(x, y):
    if x == 0:
        print("you can't choose from nothing")
        return None
    if y > x:
        print("that's not a combination problem")
        return None
    z = x - y
    NcR = function_factorial(x) / (function_factorial(y) * function_factorial(z))

    return NcR


Combinations = function_NcR(50, 20)
if Combinations is not None:
    print("the number of combinations is", Combinations)
