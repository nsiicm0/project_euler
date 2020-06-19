'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math

def max_prime_factor(n:int) -> int:
    max_p = 0
    while n % 2 == 0:
        max_p = 2
        n = n / 2
    # now we are no longer even
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            max_p = i
            n = n / i 
    
    # whatever is left is now a prime number
    if n > 2:
        max_p = n

    return max_p

n = 600851475143
print(max_prime_factor(n))