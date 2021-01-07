import hashlib
from pearhash import PearsonHasher

# Input: position inside shingles set
# Support Libraries: hashlib
# Support Function: hash, it generates the hash function using SHA1 algorithm, SHA256\SHA512\SHA3_512 and SHA3_256 algorithms
#         are inefficient and their complexity is not needed here.
# Output: returns an hash function to use for each shingle, each hash function is unique


## TEST 1: SHA256 with big dataset key mismatch in cluster algorithm
## TEST 2: SHA1 with big dataset with 2K pages: OK! -> Switch to SHA1: Vectorization in 373sec without key errors in cluster algorithm
## TEST 3: SHA1 with entire TMDB dataset (2K Movies, 2K TVSeries, 1.5K Actors): Over 2h of execution. abort.
## TEST 4: BLAKE2b algorithm implementation, fastest than SHA1 in theory: 1K Movies, 1K TVSeries, 1K Actors OK! 301sec Vectorization
## TEST 5: BLAKE2b algorithm implementation with entire TMDB dataset: TODO 

def hashFunction(n):
  def hash(x):
    output = hashlib.blake2b(str(x).encode('utf-8')).hexdigest()
    for i in range(n):
      output = hashlib.blake2b(str(x).encode('utf-8')).hexdigest()
    return output[:8]
  return hash

## Test 1: Vectorization small dataset: 64sec 
## Test 2: Vectorization big dataset: No key error but executed in 2441.22 sec

def hashFunction_1ByteShingle(n):
  def hash(x):
    hashFunction = PearsonHasher(1)
    output = "".join(x)
    b = hashFunction.hash(bytes(output, encoding='utf-8'))
    while range(n):
      b = hashFunction.hash(b)
    return output[:8]
  return hash


# Input: shingles set
# Support Function: hashFunction
# Ouput: vector of hashed shingles

def shingleVectorizer(shingles):
    shinglesVector = []
    for i in range(8):
        hash = hashFunction(i)
        shingleHashes = []
        for shingle in shingles:
            shingleHashes.append(hash(shingle)) 
        minHash = min(shingleHashes)
        shinglesVector.append(minHash)
    return shinglesVector