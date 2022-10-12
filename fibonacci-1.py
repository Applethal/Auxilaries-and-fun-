def Fibonacci(x):
    if x > 2:
        return Fibonacci(x - 1) + Fibonacci(x - 2)
    if x == 0:
        return 0
    else:
        return 1


y = Fibonacci(int(input()))
print(y)
