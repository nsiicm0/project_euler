'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def sieve_prime_generator():
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

n = 10001
print(next(x for i,x in enumerate(sieve_prime_generator()) if i==n-1)) # n - 1 to adjust for 0 based enumerate