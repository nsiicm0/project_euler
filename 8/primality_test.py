import math
def is_prime(n:int) -> bool:
    if n == 1: return False
    if n < 4: return True # 2 and 3 are prime
    if n % 2 == 0: return False # there are no even primes at this point
    if n < 9: return True # 4, 6 and 8 have already been excluded
    if n % 3 == 0: return False
    r = math.floor(math.sqrt(n)) # satisifes the condition of r*r <= n
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f=f+6
    return True

print(is_prime(67280421310721))