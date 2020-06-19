'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def aliquot(n: int):
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

limit = 10000
# Two numbers m and n are said to be an Amicable Pair if σ(m)−m=n and σ(n)−n=m.
# http://mathonline.wikidot.com/aliquot-sequences-amicable-pairs-and-sociable-numbers
#print( sum( n for n in range( 2, limit) if aliquot( aliquot( n)) == n and aliquot( n) != n)) # this also works but not really understandable
amicable_dict = dict()
for i in range(limit):
    amicable_dict[i] = aliquot(i)

set1 = set()
set2 = set()
for k, v in amicable_dict.items():
    if k != v:
        set1.add((k,v))
        set2.add((v,k))

unique_pairs = []
for e1, e2 in set1.intersection(set2):
    if (e1, e2) not in unique_pairs and (e2, e1) not in unique_pairs:
        unique_pairs.append((e1,e2))

cumsum = 0
for e1, e2 in unique_pairs:
    cumsum += e1 + e2

print(cumsum)