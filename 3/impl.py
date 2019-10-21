#!/bin/python3

import sys
import math

t = int(input().strip())

def find_max_prime_factor(n):
    max_p = 0

    # Test n for the only even prime number
    # Basically, iterate as long until no longer divisible.
    while n % 2 == 0:
        max_p = 2
        n = n / 2
    
    # Only odd numbers left now, hence we start at 3 and increment by 2
    # Test until sqrt of n.
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            max_p = i
            n = n / i 
    
    # Anything left is now a prime number
    if n > 2: 
        max_p = n 
    
    return int(max_p)


for a0 in range(t):
    n = int(input().strip())
    p = None
    print(find_max_prime_factor(n))
