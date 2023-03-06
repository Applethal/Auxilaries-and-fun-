#n = int(input("Enter the number to be checked."))


def Prime_check(n):

    check = n
    list = []
    Prime = True
    while check > 0:
        prime_test = n / check
        if n % check == 0:
            list.append(prime_test)
        else:
            pass
        check -= 1

    if len(list) == 2:
        #print("Yes, the number is a prime number")
        Prime = True

    else:
        #print("The number is not a prime number")
        Prime = False

    return Prime


N = int(input("What prime number are you looking for ?"))


def Prime_n(N):
    counter = 0
    num = 1
    while counter < N:
        num += 1
        if Prime_check(num):
            counter += 1

    print("The requested number is ", num)


Prime_n(N)
