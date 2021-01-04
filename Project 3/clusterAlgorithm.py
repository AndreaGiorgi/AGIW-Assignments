from merge_sort import mergeSort

# Algorithm structure
#
#	First pass: Initialize hash table and create 8/8, 7/8, 6/8 masked shingles vectors
#				 7/8 and 6/8 vectors has None as wildcard
#	Second pass: Order all 8/8 shingle vecor and for each one select a candidate 
# 				  with the largest count in H and decrements remaining candidates 
# 				  by 8/8 cluster size. 
# 	Third pass: Final assignments of pages to cluster without adjusting vector count	
# 

THRESHOLD = 2 #Should be 20 when we parse all 3K pages
WILDCARD = None

# FIRST PASS 

def initMaskedVectors(shingleVector):
	mskVectors = []
	#8/8
	mskVectors.append(shingleVector)
	
	#7/8
	for element in shingleVector:
		vector = []
		for shingle in shingleVector:
			if(element == shingle):
				vector.append(WILDCARD)
			else:
				vector.append(shingle)
		mskVectors.append(vector)

	#6/8
	vector = []
	for element in shingleVector:
		vector.append(element)

	combinations = []
	for i in range(len(shingleVector)):
		for j in range(len(shingleVector)):
			if i != j and not ((j,i) in combinations):
				combinations.append((i,j))

	for (i,j) in combinations:
		auxVector = vector.copy()
		auxVector[i] = WILDCARD
		auxVector[j] = WILDCARD
		mskVectors.append(auxVector)
		
	return mskVectors


def initMaskedhashTables(pages, hashTable):
	for page in pages:
		shingleVector = page.shingleVector
		maskedShingleVectors = initMaskedVectors(shingleVector)

		for masked in maskedShingleVectors:
			masked = tuple(masked)
			if not masked in hashTable:
				hashTable[masked] = 1
			else:
				maskedCount = hashTable[masked]
				maskedCount += 1
				hashTable[masked] = maskedCount

# SECOND PASS

def isCoverVector(shingleVector, coverCandidate):
	for i in range(len(shingleVector)):
		if shingleVector[i] != coverCandidate[i] and coverCandidate[i] != WILDCARD:
			return False
	return True


def decrementCounts(hashTable):

	eightShingleVectors = list(filter(lambda x: (WILDCARD not in x), hashTable.keys()))
	mergeSort(eightShingleVectors, 0, len(eightShingleVectors) -1, hashTable)
	maxShingleVectors = {}

	for esv in eightShingleVectors:
		esv = tuple(esv)
		max = 0
		maxShingleVector = None

		for shingleVector in hashTable.keys():
			if isCoverVector(esv, shingleVector) and max < hashTable[shingleVector]:
				max = hashTable[shingleVector]
				maxShingleVector = shingleVector

		maxShingleVectors[esv] = maxShingleVector

		for shingleVector in hashTable.keys():
			if isCoverVector(esv, shingleVector) and maxShingleVector != shingleVector:
				aux = hashTable[shingleVector]
				aux -= hashTable[esv]
				if aux < 0:
					aux = 0
				hashTable[shingleVector] = aux
	
	keys = list(hashTable.keys()).copy()
	for shingleVector in keys:
		if hashTable[shingleVector] < THRESHOLD:
			hashTable.pop(shingleVector)
	
	return maxShingleVectors

# THIRD PASS

def createClusters(hashTable, pages, maxShingleVectors):
	clusters = {}
	
	for shingleVector in hashTable.keys():
		clusters[shingleVector] = []
	
	for page in pages:
		shingleVector = page.shingleVector
		maxShingleVector = maxShingleVectors[shingleVector]
		clusters[maxShingleVector].append(page)
	
	pageClusters = []
	
	for key in clusters.keys():
		group = clusters[key]
		if len(group) != 0:
			pageClusters.append(group)

	return pageClusters

# Algorithm Pipeline

def startAlgorithm(pages):

	hashTable = {}
	initMaskedhashTables(pages, hashTable)
	maxShingleVectors = decrementCounts(hashTable)
	return createClusters(hashTable, pages, maxShingleVectors)
