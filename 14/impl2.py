'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import math

def colatz_count(start: int, cache: dict) -> int:
    if start == 1:
        return 1
    else:
        if start in cache:
            return cache[start]
        else:
            if start % 2 == 0:
                count_to_start = 1 + colatz_count(start // 2, cache)
                cache[start] = count_to_start
                return count_to_start
            else:
                # saving a step
                count_to_start = 2 + colatz_count((3 * start + 1) // 2, cache)
                cache[start] = count_to_start
                return count_to_start

n = 1000000
longest_series = (1,1)
cache = {}
for i in range(n, math.floor(n/2)-1, -1):
    _count = colatz_count(i, cache)
    if _count > longest_series[1]:
        longest_series = (i,_count)
print(longest_series[0])