import time, operations

def pipeline():
	startedAt = time.time()
	paths = operations.initialization()
	pages = operations.vectorization(startedAt, paths)
	computedClusters =	operations.clustering(startedAt, pages)
	operations.evaluation(pages, computedClusters)

if __name__ == '__main__':
   pipeline()