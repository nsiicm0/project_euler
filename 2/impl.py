#!/bin/python3

import sys
from functools import reduce

def gen_fib(n):
    a,b = 0,1
    while True:
        if a >= n:
            break
        yield a
        a, b = b, a + b

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    # Generate Fibonacci sequence, filter out odd numbers and sum remaining numbers
    print(reduce(lambda x,y: x+y, filter(lambda x: x % 2 == 0, gen_fib(n))))
