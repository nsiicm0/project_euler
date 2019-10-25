#!/bin/python3

import sys
import itertools

def sieve_generator():
    '''
        Sieve of Erastothenes Generator.
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
        
def sieve_generator2():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthene.
    '''
    composites = dict()

    # skipping first prime
    yield 2
    
    for candidate in itertools.islice(itertools.count(3), 0, None, 2):
        hit = composites.pop(candidate, None)
        if hit is None:
            # candidate is prime case
            composites[candidate * candidate] = 2 * candidate 
            yield candidate
        else:
            # candidate is not prime case
            x = hit + candidate
            while x in composites:
                x += hit
            composites[x] = hit

def find_nth_prime(n):
    for i, prime in enumerate(sieve_generator()):
        if i+1 == n:
            return prime

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_nth_prime(n))
