def function_even(x):
    y = x - 1
    while y > 1:
        y -= 2

    if y == 0:
        print("Odd")
    else:
        print("Even")
    return y


function_even(1)
