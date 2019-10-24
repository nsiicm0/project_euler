#!/bin/python3

import sys

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

def find_nth_prime(n):
    for i, prime in enumerate(sieve_generator()):
        if i+1 == n:
            return prime

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_nth_prime(n))
