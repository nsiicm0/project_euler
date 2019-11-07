from functools import reduce

def char_position(letter):
    return ord(letter.lower()) - 96

def get_score(sorted_names):
    total_score = 0
    for position, name in enumerate(sorted_names):
        _char_sum = reduce(lambda x,y: x+y, map(char_position, name))
        total_score += (position + 1) * _char_sum
    return total_score

t = int(input().strip())
names = []
for _ in range(t):
    names.append(list(input().strip()))
sorted_names = sorted(names)
print(get_score(sorted_names))