#!/bin/python3

import sys
from functools import reduce

t = int(input().strip())

# Evolution 1
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def divisible_3(n):
    return True if sum_digits(sum_digits(n)) in [3,6,9] else False

def divisible_5(n):
    return True if repr(n)[-1:] in ['0', '5'] else False

def test_for_multiplicity(n):
    for i in range(n):
        if divisible_5(i) or divisible_3(i):
            yield i

# Evolution 2
def generate_numbers(upperbound):
    '''
        Approach to generate only numbers which are divisible by 3 or 5
    '''
    _subtotal3 = 3
    _subtotal5 = 5
    while min([_subtotal3, _subtotal5]) < upperbound:
        if _subtotal3 == _subtotal5:
            yield _subtotal3
            _subtotal3 += 3
            _subtotal5 += 5
        elif _subtotal3 < _subtotal5:
            yield _subtotal3
            _subtotal3 += 3
        elif _subtotal3 > _subtotal5:
            yield _subtotal5
            _subtotal5 += 5

# Evolution 3
def calc_sum(n):
    '''
        Fastest way. Use Eulers method of calculating the sum of all numbers leading up to n (including n)
    '''
    div_3 = (((n // 3)) * (2 * 3 + (n // 3 - 1) * 3) // 2) 
    div_5 = (((n // 5)) * (2 * 5 + (n // 5 - 1) * 5) // 2) 
    div_15 = (((n // 15)) * (2 * 15 + (n // 15 - 1) * 15) // 2)
    return div_3 + div_5 - div_15

for a0 in range(t):
    n = int(input().strip())
    print(calc_sum(n-1))
