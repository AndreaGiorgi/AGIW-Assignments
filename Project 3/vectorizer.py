import hashlib
from pearhash import PearsonHasher

# Input: position inside shingles set
# Support Libraries: hashlib
# Support Function: hash, it generates the hash function using SHA256 algorithm, SHA512\SHA3_512 and SHA3_256 algorithms
#         are 0.5/0.3s slower
# Output: returns an hash function to use for each shingle, each hash function is unique

def hashFunction(n):
  def hash(x):
    x = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
    for i in range(n):
      x = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
    b = bytes(x[:8], encoding='utf-8')
    output = int.from_bytes(b, byteorder='big', signed=False)
    return output
  return hash


## ANDREA: Prima prova di hash 8Byte dove ogni shingle ha un hash di 1Byte
## Test 1: Vectorization: 64sec [Molto Lento]

def hashFunction_1byteShingle(n):
  def hash(x):
    hashFunction = PearsonHasher(1)
    x = "".join(x)
    b = hashFunction.hash(bytes(x, encoding='utf-8'))
    for i in range(n):
      b = hashFunction.hash(b)
    output = int.from_bytes(b, byteorder='big', signed=False)
    return output
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