'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def sieve_prime_generator() -> int:
    '''
        Sieve of Erastothenes Generator.
        This is a really fast and memory efficient prime generator.
    '''
    composites = dict()
    candidate = 2   # first integer to test for primality
    while True:
        if candidate not in composites.keys():
            # candidate must be prime
            yield candidate 
            # mark the first multiple as composite
            composites.setdefault(candidate+candidate, [candidate]).append(candidate)
        else:
            # advance composites to the next bigger multiple
            for composite in composites[candidate]: 
                composites.setdefault(composite+candidate,[]).append(composite)
            # We are past the candidate, so we can delete it
            del composites[candidate]
        candidate += 1

limit = 2000000
cumsum = 0
prime_gen = sieve_prime_generator()
prime = next(prime_gen)
while prime < limit:
    cumsum += prime
    prime = next(prime_gen)

print(cumsum)