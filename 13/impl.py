from functools import reduce

t = int(input().strip())
numbers = []
for _ in range(t):
    numbers.append(int(input().strip()))
sum_ = reduce(lambda x,y: x+y, numbers)
print(repr(sum_)[:10])