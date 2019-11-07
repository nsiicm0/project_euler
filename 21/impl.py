import math
from functools import reduce

def get_proper_divisors(n):
    blacklist = [n]
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i not in blacklist:
                yield i
                blacklist.append(i)
            if n // i not in blacklist:
                yield n // i
                blacklist.append(n//i)
    
def d(n):
    try:
        return reduce(lambda x,y: x+y, get_proper_divisors(n))
    except:
        return 0

def find_amicable_number(limit):
    for a in range(1, limit):
        for b in range(a+1, limit+1):
            if d(a) == b and d(b) == a:
                yield a, b

t = int(input().strip())
for _ in range(t):
    limit = int(input().strip())
    amicable_numbers = list(reduce(list.__add__, ([a,b] for a,b in find_amicable_number(limit))))
    print(reduce(lambda x,y: x+y, amicable_numbers))