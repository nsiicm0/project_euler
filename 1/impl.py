#!/bin/python3

import sys

t = int(input().strip())

def test_for_multiplicity(n):
    for i in range(n):
        if i % 5 == 0 or i % 3 == 0:
            yield i

for a0 in range(t):
    n = int(input().strip())
    print(sum(test_for_multiplicity(n)))
