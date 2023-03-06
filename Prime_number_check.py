n = int(input("Enter the number to be checked."))



check = n 
list = []
while check > 0:
    prime_test = n / check
    if n % check == 0:
        list.append(prime_test)
    else:
        pass
    check -= 1

if len(list) == 2:
    print("Yes, the number is a prime number")
else:
    print("The number is not a prime number")


## what is the n'th prime number 
    
prime_numbers = []

N = int(input("Input the position of the prime that you wish to know ?"))

while prime_numbers[-1] == N:
