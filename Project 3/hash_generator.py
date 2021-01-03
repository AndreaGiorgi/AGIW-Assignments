import hashlib

#It creates a different hash function for each distinct n
def generate_hash_function(n):
  def myhash(x):
    output = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
    for i in range(n):
      output = hashlib.sha256(str(output).encode('utf-8')).hexdigest()
    return output[:8]

  return myhash

def generate_hash_function2(n):
  def myhash(x):
    output = hash(x)
    for i in range(n):
      output = hash(output)
    return output

  return myhash