import time, operations

def executionPipeline(path):
	startedAt = time.time()
	paths = operations.getPaths(path)
	vectorizedPages = operations.vectorization(startedAt, paths)
	computedClusters = operations.clustering(startedAt, vectorizedPages)
	operations.evaluation(vectorizedPages, computedClusters)
 
if __name__ == '__main__':
	path = input("Choose Dataset [Dataset_TMDB\Dataset_Study\Dataset_G2R]: ")
	executionPipeline(path)