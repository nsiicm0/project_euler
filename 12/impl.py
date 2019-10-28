from math import floor, sqrt
from functools import reduce

def get_triangular_numbers():
    '''maybe use n*(n+1)/2'''
    _running_sum = 0
    x = 0
    while True:
        x += 1
        _running_sum += x
        yield _running_sum

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

def find_factors_until_threshold(number, threshold):
    factors = [1]
    sieve = sieve_generator()
    testable = next(sieve)
    while testable <= number:
        if number % testable == 0:
            factors.append(testable)
            # test all multiple until number/2
            for _test in range(testable+testable, number+1, testable):
                if number % _test == 0 and _test not in factors:
                    factors.append(_test)
            if len(factors) > threshold:
                return True
        testable = next(sieve)
        while testable in factors:
            testable = next(sieve)
    return False

def find(factor_threshold):
    number_generator = get_triangular_numbers()
    while True:
        number = next(number_generator)
        if find_factors_until_threshold(number, factor_threshold):
            return number
        
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(find(n))
