#!/bin/python3

import sys
from functools import reduce

def calc(n):
    left = reduce(lambda x, y: x+y, range(1,n+1))**2
    # the right side is the equivalent of a Pyramidal number, thus special rules apply
    right = (n*(n+1)*(2*n+1))//(6)
    return left - right

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(calc(n))