'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
from functools import reduce

n = 1000
p = pow(2,n)
print(reduce(lambda x,y: x+y, list(map(int, list(repr(p))))))