from math import floor

def colatz_verbose(start: int) -> str:
    if start == 1:
        return '{}'.format(start)
    else:
        if start % 2 == 0:
            return '{} > {}'.format(start, colatz_verbose(start // 2))
        else:
            return '{} > {}'.format(start, colatz_verbose(3 * start + 1))

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
    

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    longest_series = (1,1)
    cache = {}
    for i in range(n, floor(n/2)-1, -1):
        _count = colatz_count(i, cache)
        if _count > longest_series[1]:
            longest_series = (i,_count)
    print(longest_series[0])
