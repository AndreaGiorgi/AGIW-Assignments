import time, operations

def executionPipeline():
	startedAt = time.time()
	paths = operations.getPaths()
	vectorizedPages = operations.vectorization(startedAt, paths)
	computedClusters =	operations.clustering(startedAt, vectorizedPages)
	operations.evaluation(vectorizedPages, computedClusters)

def testPipeline():
	startedAt = time.time()	
 
if __name__ == '__main__':
    executionPipeline()
    #testPipeline()