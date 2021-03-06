'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
import math
from typing import Dict
from functools import reduce

def sieve_prime_generator() -> int:
    '''
        Sieve of Erastothenes Generator.
        This is a really fast and memory efficient prime generator.
    '''
    composites = dict()
    candidate = 2   # first integer to test for primality
    while True:
        if candidate not in composites.keys():
            # candidate must be prime
            yield candidate 
            # mark the first multiple as composite
            composites.setdefault(candidate+candidate, [candidate]).append(candidate)
        else:
            # advance composites to the next bigger multiple
            for composite in composites[candidate]: 
                composites.setdefault(composite+candidate,[]).append(composite)
            # We are past the candidate, so we can delete it
            del composites[candidate]
        candidate += 1

def triangle_number(n:int) -> int:
    return n * (n + 1) // 2

def get_factors(n:int) -> Dict:
    factors = dict()
    prime_generator = sieve_prime_generator()
    prime_candidate = next(prime_generator)
    while n != 1: 
        magnitude = 0
        while (n % prime_candidate == 0): 
            n = n // prime_candidate
            magnitude += 1
        factors[prime_candidate] = magnitude
        prime_candidate = next(prime_generator)
    return factors

limit = 500
i=2
while True:
    T = triangle_number(i)
    factors = get_factors(T)
    if sum(factors.values())>=500:
        print(i-1)
        print(T)
        break
    i+=1

# This can be made faster by caching the prime numbers