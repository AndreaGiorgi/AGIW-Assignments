from hash_generator import generate_hash_function
from hash_generator import generate_hash_function2

"""
It finds the minimum hash among 
the shingles passed as parameters
"""
def get_min_hash(shingles, h):
    hashes = []
    for shingle in shingles:
        hashes.append(h(shingle))

    return min(hashes)

"""
It converts a shingle set to a vector
operating a message digest with generated 
cryptographic hases
"""
def shingles_to_vectors(shingles):
    v = []
    for i in range(8):
        h = generate_hash_function(i)
        min_hash = get_min_hash(shingles,h)
        v.append(min_hash)
    return v

