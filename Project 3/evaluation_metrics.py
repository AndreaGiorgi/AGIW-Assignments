def get_all_possible_couples(elements):
    couples = []
    for elem1 in elements:
        for elem2 in elements:
            if(elem2,elem1) not in couples and elem1 != elem2:
                couples.append((elem1, elem2))
    return couples

def cluster_to_pair(clusters):
    output = []
    for cluster in clusters:
        for couple in get_all_possible_couples(cluster):
            output.append(couple)
    return set(output)



def intersection(set1, set2):
    output = []
    for elem in set1:
        if elem in set2:
            output.append(elem)
    return output


def difference(set1, set2):
    output = []
    for elem in set1:
        if elem not in set2:
            output.append(elem)
    return output


"""
Computes the f1score for pair clustering 
"""
def f1score(true_clusters, actual_clusters):
    couples1 = cluster_to_pair(true_clusters)
    couples2 = cluster_to_pair(actual_clusters)
    inter = len(intersection(couples1,couples2))
    diff1 = len(difference(couples1,couples2))
    diff2 = len(difference(couples2,couples1))
    return (2 * inter) /(2 * inter + diff1 + diff2)

