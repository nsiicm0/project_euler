from functools import reduce
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    p = pow(2,n)
    print(reduce(lambda x,y: x+y, list(map(int, list(repr(p))))))