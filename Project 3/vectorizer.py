import hashlib

# Input: position inside shingles set
# Support Libraries: hashlib
# Support Function: hash, it generates the hash function using SHA256 algorithm, SHA512\SHA3_512 and SHA3_256 algorithms
#         are 0.5/0.3s slower
# Output: returns an hash function to use for each shingle, each hash function is unique

def hashFunction(n):
  def hash(x):
    output = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
    for i in range(n):
      output = hashlib.sha256(str(output).encode('utf-8')).hexdigest()
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