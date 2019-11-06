import math
from functools import reduce

def get_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n)+1)) if not n % i)
        
def generate_triangles():
    l = 1
    while True:
        yield sum(range(l + 1))
        l += 1

def test_triangles(limit):
    for i in generate_triangles():
        if get_factors(i) > limit and i > 1:
            return i

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(test_triangles(n))
