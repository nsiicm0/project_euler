'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

n = 20

def get_test_numbers(n:int) -> int:
    '''We will only test the largest multiples
    for instance we will not test 2 and 4 if we are gonna test 8.
    '''
    candidates = range(2, n+1)
    for i, candidate in enumerate(candidates):
        ret = True
        for next_candidate in candidates[i+1:]:
            if next_candidate % candidate == 0:
                ret = False
                break
        if ret:
            yield candidate

def find_number(n:int) -> int:
    factors_to_test = list(get_test_numbers(n))[::-1]
    increment = max(factors_to_test) # we will search the number by incrementing the maximum number
    if len(factors_to_test) == 1:
        return factors_to_test[0]
    number = 0
    divisible = len(factors_to_test[1:]) * [False]
    while not all(divisible):
        number += increment
        divisible = len(factors_to_test[1:]) * [False]
        for i, factor in enumerate(factors_to_test[1:]): # skipping the first one - no need to test
            if number % factor == 0:
                divisible[i] = True
            else:
                break
            
    return number

print(find_number(n))