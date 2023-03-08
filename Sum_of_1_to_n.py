#With recursion

n = int(input("Input the n"))


def sum(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n + sum(n - 1)


print(sum(n))


### no recursion
def Sum(n):

    i = 1
    counter = 0
    while counter != n + 1:

        i += counter
        counter += 1
    i -= 1
    return i


print(Sum(n))
