from itertools import permutations

def string_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))