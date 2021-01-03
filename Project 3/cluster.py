from merge_sort import mergeSort

THRESHOLD = 2

#Find all the possible couples
def get_all_possible_couples(number):
    pairs = []
    for i in range(number):
        for j in range(number):
            if i != j and not ((j,i) in pairs):
                pairs.append((i,j))
    return pairs

#Find all the masked shingle vectors with None as wildcard
def get_masked_shingle_vectors(shingle_vector):
    masked_vectors = []
    #we add the 8/8 masked shingle vector
    masked_vectors.append(shingle_vector)

    #we add all the 7/8 masked shingle vectors
    for elem in shingle_vector:
        v = []
        for sv in shingle_vector:
            if(sv == elem):
                v.append(None)
            else:
                v.append(sv)

        masked_vectors.append(v)


    #we add all the 6/8 masked shingle vectors
    v = []
    for elem in shingle_vector:
        v.append(elem)


    for (i,j) in get_all_possible_couples(len(shingle_vector)):
        l = v.copy()
        l[i] = None
        l[j] = None
        masked_vectors.append(l)

    return masked_vectors

"""
It checks if the cover vector covers 
the shingle_vector
"""
def is_cover(shingle_vector, cover):
    for i in range(len(shingle_vector)):
        if shingle_vector[i]!=cover[i] and cover[i] != None:
            return False
    return True

"""
Find all the 8-shingle vectors and order them 
performing merge sort algorithm
"""
def get_8_shingle_vector(hashTable):
    shingle_vectors = list(filter(lambda l: (None not in l), hashTable.keys()))
    mergeSort(shingle_vectors,0, len(shingle_vectors)-1, hashTable)
    return shingle_vectors

"""
Initialize the hash table with the masked shingle vectors
"""
def initializeTable(pages, hashTable):
    for page in pages:
        shingle_vector = page.shingle_vector
        masked_shingle_vectors = get_masked_shingle_vectors(shingle_vector)

        for msv in masked_shingle_vectors:
            #convert to tuple to be keys
            msv = tuple(msv)
            if not msv in hashTable:
                hashTable[msv] = 1
            else:
                count = hashTable[msv]
                count += 1
                hashTable[msv] = count


"""
Second pass of the clustering algorithm
"""
def decrementCounts(hashTable):
    #find all the eight shingle vectors in increasing order of counts
    eight_shingle_vectors = get_8_shingle_vector(hashTable)
    max_shingle_vectors = {}
    #iterate over all the eight shingle vectors
    for esv in eight_shingle_vectors:
        esv = tuple(esv)
        max_count = 0
        max_shingle_vector = None
        #iterate over the keys and finds the cover with the maximum counts
        for sv in hashTable.keys():
            if is_cover(esv,sv) and max_count < hashTable[sv]:
                max_count = hashTable[sv]
                max_shingle_vector = sv

        max_shingle_vectors[esv] = max_shingle_vector


        #decrement the counts of all the other coverings
        for sv in hashTable.keys():
            if is_cover(esv, sv) and max_shingle_vector != sv:
                count = hashTable[sv]
                count -= hashTable[esv]
                if count < 0:
                    count = 0
                hashTable[sv] = count

    keys = list(hashTable.keys()).copy()
    #remove the elements under the threshold
    for sv in keys:
        if hashTable[sv] < THRESHOLD:
            hashTable.pop(sv)

    return max_shingle_vectors

"""
The main function of the clustering algorithm
"""
def cluster(pages):
    hashTable = {}
    #First pass
    initializeTable(pages, hashTable)

    #Second pass
    max_shingle_vectors = decrementCounts(hashTable)

    #Third pass
    clusters = {}

    #Initialize clusters
    for sv in hashTable.keys():
        clusters[sv] = []

    #fill the clusters
    for p in pages:
        sv = p.shingle_vector
        max_sv = max_shingle_vectors[sv]
        clusters[max_sv].append(p)

    page_clusters = []
    #return the non-empty clusters
    for key in clusters.keys():
        group = clusters[key]
        if len(group) != 0:
            page_clusters.append(group)

    return page_clusters