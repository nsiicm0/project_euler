'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math
from functools import reduce

def triplets(limit:int) -> tuple:
    for a in range(1, limit):
        b = a + 1
        c = b + 1
        while a + b + c <= limit:
            while c * c < a * a + b * b:
                c += 1
            if c * c == a * a + b * b and a + b + c <= limit:
                yield (a, b, c)
            b += 1                                                           

n = 1000
for a,b,c in triplets(n):
    if a + b + c == n:
        print(a*b*c)
        