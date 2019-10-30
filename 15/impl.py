from math import factorial

def binomial(x, y):
    try:
        binom = factorial(x) // factorial(y) // factorial(x - y)
    except ValueError:
        binom = 0
    return binom

t = int(input().strip())
for _ in range(t):
    n, m = map(int,input().split(' '))
    # for lattice path, the number of possible paths are represented by the binomial coefficient
    print(binomial(n+m,n))