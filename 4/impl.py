#!/bin/python3

import sys

def is_palindrome(n):
    return repr(n) == repr(n)[::-1]

def complies_with_division_constraint(n):
    '''
        Palindrome has to be the product of 2 3 digit numbers.
        We use some pruning technique below. 
        As soon as a division might go over 1000 as a result, we prune.
        Because the lower the 3 digit number becomes, the bigger the chance the result is 4 digit.
    '''
    for i, divisor_1 in enumerate(range(900,0,-100)):
        if n / divisor_1 >= 1000 and i != 0:
            break
        else:
            for j, divisor_2 in enumerate(range(divisor_1+90, divisor_1-1,-10)):
                if n / divisor_2 >= 1000 and j != 0:
                    break
                else:
                    for divisor_3 in range(divisor_2+9, divisor_2-1, -1):
                        if n % divisor_3 == 0:
                            return True

def find_palindrome(n):
    for candidate in range(n-1, 99999, -1):
        if is_palindrome(candidate):
            if complies_with_division_constraint(candidate):
                return candidate

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_palindrome(n))
