import time, operations

def testPipeline(path):
	startedAt = time.time()
	print("Testing  " + path)
	paths = operations.getPaths(path)
	vectorizedPages = operations.vectorization(startedAt, paths)
	computedClusters = operations.clustering(startedAt, vectorizedPages)
	operations.evaluation(vectorizedPages, computedClusters)

## TODO: Multithreading?

if __name__ == '__main__':
	datasets = ["Dataset_TMDB", "Dataset_Study", "Dataset_G2R"]
	for dataset in datasets:
		testPipeline(dataset)