from itertools import permutations

def get_permutations(objects):
    return permutations(objects)

def sort_permutation(gen_object):
    for elem in sorted(gen_object):
        yield elem

if __name__ == "__main__":
    #objects = [3,1,2]
    objects = [0,1,2,3,4,5,6,7,8,9]
    for i, elem in enumerate(sort_permutation(get_permutations(objects))):
        if i == 999999:
            print(''.join(map(str,list(elem))))
            break