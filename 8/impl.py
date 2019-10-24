#!/bin/python3

import sys
from functools import reduce

def get_sub_num(num, n, k):
    ns = num
    for i, _ in enumerate(range(k,n+1)):
        sub_num = ns[i:i+k]
        if '0' not in sub_num:
            yield reduce(lambda x,y: int(x)*int(y), sub_num)
        else:
            yield 0

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    if n <= k or (n == k and '0' in num):
        print(0)
    else:
        print(max(list(get_sub_num(num,n,k))))
