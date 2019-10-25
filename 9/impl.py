#!/bin/python3

import sys
import math
from functools import reduce

def find_triplet(n):
    for b in range(n):
        for a in range(1, b):
            c = math.sqrt( pow(a,2) + pow(b,2))
            if c % 1 == 0:
                return [a, b, int(c)]
    return [-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(reduce(lambda x,y: x*y, find_triplet(n)))