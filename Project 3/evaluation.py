def executionTime(endTime, startTime):
    elapsedTime = endTime - startTime
    return elapsedTime

def cluster2pairs(clusters):
    output = []
    for cluster in clusters:
        combinations = []
        for i in cluster:
            for j in cluster:
                if(j,i) not in combinations and i != j:
                    combinations.append((i,j))
        for couple in combinations:
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

# Precision metric TP/(TP+FP)

def precision(idealClusters, computedClusters):
    idealPairs = cluster2pairs(idealClusters)
    computedPairs = cluster2pairs(computedClusters)
    truePositive = len(intersection(idealPairs, computedPairs))
    falsePositive = len(difference(computedPairs, idealPairs))
    return truePositive/(truePositive + falsePositive)

#Recall metric TP/(TP+FN)

def recall(idealClusters, computedClusters):
    idealPairs = cluster2pairs(idealClusters)
    computedPairs = cluster2pairs(computedClusters)
    truePositive = len(intersection(idealPairs, computedPairs))
    falseNegative = len(difference(idealPairs, computedPairs))
    return truePositive/(truePositive + falseNegative)

# F1 Measure metric, 2*(Precison*Recall)/(Precision+Recall)

def f1(precision, recall):
    return 2 * ((precision*recall)/(precision + recall))

