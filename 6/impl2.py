'''
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

from functools import reduce

n = 100

def calc(n:int) -> int:
    '''We are trying to find the sum of squares up to n minus the square of the sum up to n.
    '''
    # sum of squares is the special case of "Square Pyramidal Numbers"
    sum_of_squares = (n * (n + 1) * (2 * n + 1))/6

    square_of_sums = reduce(lambda x,y: x+y, range(1,n+1))**2

    return int(abs(sum_of_squares-square_of_sums))

print(calc(n))