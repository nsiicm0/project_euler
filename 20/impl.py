from functools import reduce

def factorial(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_digits(n):
    return reduce(lambda x,y: x+y, map(int, list(repr(n))))

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(sum_digits(factorial(n)))
