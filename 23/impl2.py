'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import itertools

def aliquot(n: int) -> int:
    '''An Aliquot Sum is the sum of the proper divisors of n
    https://en.wikipedia.org/wiki/Aliquot_sum
    '''
    acc = 1
    for i in range( 2, n):
        if n % i == 0:
            if i > n // i: break
            acc += i + n // i
            if i == n // i: 
                acc -= i
    return acc

def classify(n: int) -> str:
    res = aliquot(n)
    if res == n: return "PERFECT"
    if res < n: return "DEFICIENT"
    if res > n: return "ABUNDANT"

limit = 28123
abundant_numbers = []
for i in range(1,limit+1):
    if classify(i) == 'ABUNDANT':
        abundant_numbers.append(i)

cumsum = 0
for i in range(1, limit+1):
    can_be_written = False
    possible_summands = list(itertools.compress(abundant_numbers, map(lambda x: x<i, abundant_numbers)))
    for j in possible_summands:
        if i - j in possible_summands:
            can_be_written = True
            break
    if not can_be_written:
        cumsum += i
print(cumsum)