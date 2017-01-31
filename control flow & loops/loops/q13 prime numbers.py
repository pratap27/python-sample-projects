# python program to find prime numbers

''' num = int(input('Enter a numeber: '))

# prime numbers are greater than 1

if num > 1:
    for i in range(2,num):
        if (num%i) == 0:
            print(num, 'is not a prime number')

            print(i,'times', num//i, 'is: ', num)
            break

    else:
        print(num, 'is a prime number')

else:
   print(num,"is not a prime number") '''
# first one
def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True


# second one

import math
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for x in range(3, sqr, 2):
        if n % x == 0:
            return False
    return True

''' def isprime(n):
    print('check if integer n is a prime')
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True '''



            

                
            
