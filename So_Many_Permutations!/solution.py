from itertools import permutations as it_permutations

def permutations(input_str):
    # Use set to remove duplicates, and join the characters back to form strings
    return list(''.join(p) for p in set(it_permutations(input_str)))
