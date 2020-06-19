import math
import itertools

def sieve_generator():
    '''
        Sieve of Erastothenes Generator.
    '''
    composites = dict()

    # skipping first prime
    yield 2
    
    for candidate in itertools.islice(itertools.count(3), 0, None, 2):
        hit = composites.pop(candidate, None)
        if hit is None:
            # candidate is prime case
            composites[candidate * candidate] = 2 * candidate 
            yield candidate
        else:
            # candidate is not prime case
            x = hit + candidate
            while x in composites:
                x += hit
            composites[x] = hit

def proper_divisors_sum(n):
    b = n
    product = 1
    for p in sieve_generator():
        if p > n:
            break
        i = 0
        while n % p == 0:
            n //= p
            i += 1
        if i != 0:
            product *= (p**(i + 1) - 1)//(p - 1)
    return product - b

def abundant_numbers_generator():
    for i in range(1,28123+1):
        if proper_divisors_sum(i) > i:
            yield i

def validate_abundant_number_set(abundant_numbers, N):
    number_pairs = [(x, y) for x in abundant_numbers for y in abundant_numbers] 
    return 'YES' if any(N == x+y for x,y in number_pairs) else 'NO'

if __name__ == "__main__":
    sum_ = 0
    abundant_numbers = list(abundant_numbers_generator())
    number_pairs = [(x, y) for x in abundant_numbers for y in abundant_numbers] 
    for candidate in range(28123+1):
        if not any(candidate == x+y for x,y in number_pairs):
            sum_ += candidate
    print(sum_)

'''
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if n > 28123:
        print('YES')
    else:
        print('NO')
    #print(proper_divisors_sum(n))
    #print(list(abundant_numbers_generator_under(n)))
    #print(validate_abundant_number_set(list(abundant_numbers_generator_under(n)), n))


    Here is how you proceed this Question:

Make an array say seive[0..100001]
Mark all abundant number as 1.
Extract all abundant number in another array say abundant[]
For all input N. Run a loop and check if N-abundant[i] is abundant ( seive[ N-abundant[i] ] should return 1 )?
Now the Question is How to generate Seive:

Here is some properties of abundant number:

1.	if X is perfect then all multiples of X (not X) are abundant.
2.	if X is abundant number then all multiples of X are abundant.
PS: All Integer greater than 20161 are abundant can be expressed in sum of two abundant number

28123
'''
