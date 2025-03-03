from itertools import permutations

def find_millionth_permutation():
    digits = "0123456789"
    perm = sorted(permutations(digits))  # Generate and sort all permutations
    return "".join(perm[999999])  # Index is 999999 because lists are 0-based

result = find_millionth_permutation()
print("The millionth lexicographic permutation is:", result)
