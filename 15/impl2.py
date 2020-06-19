'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
- RRDD
- RDRD
- RDDR
- DRRD
- DRDR
- DDRR

How many such routes are there through a 20×20 grid?
'''

from math import factorial

# for lattice path, the number of possible paths are represented by the binomial coefficient
# Catalan numbers give you half of the square

def catalan_numbers(n):
    ans = 1
    for k in range(2,n+1):
        ans = ans * (n+k) // k
    return ans

def binomial(x, y):
    try:
        binom = factorial(x) // factorial(y) // factorial(x - y)
    except ValueError:
        binom = 0
    return binom

n = 20
print(binomial(2*n,n)) 