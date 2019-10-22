#!/bin/python3

import sys

def find_removable_factors(factors): 
        '''
            Factors that are smaller and are an even divider of another factor, can be removed and don't need to be tested.
        '''
        for idx, factor in enumerate(factors): 
            for factor_candidate in factors[idx+1:]: 
                if factor % factor_candidate == 0: 
                    yield factor_candidate
                    
def find_number(n):
    # get factors after pruning
    factors = [f for f in range(n, 0, -1) if f not in find_removable_factors(list(range(n, 0, -1)))]
    increment = max(factors)
    _candidate = 0

    if len(factors) == 1: # handle edge case were just one factor searched
        return increment

    while True:
        _candidate += increment # always increment by largest factor
        for i, factor in enumerate(factors):
            if i == 0: # skip the first (largest) factor as we already know that it is divisible -> increment
                continue
            else:
                if _candidate % factor != 0: # back track if not fully divisible
                    break
                if i + 1 == len(factors): # if at the last factor and it was divisible we are done.
                    return _candidate

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_number(n))