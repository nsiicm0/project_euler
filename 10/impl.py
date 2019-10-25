#!/bin/python3

import sys
from functools import reduce
import itertools

def sieve_generator():
    '''
        Sieve of Erastothenes Generator.
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

def find_sum_below(n):
    for prime in sieve_generator():
        if prime <= n:
            yield prime
        else:
            break

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(reduce(lambda x,y: x+y, find_sum_below(n)))
