import time, operations, multiprocessing, logging

def testPipeline(path):
	startedAt = time.time()
	print("Testing " + path)
	paths = operations.getPaths(path)
	vectorizedPages = operations.vectorization(startedAt, paths)
	computedClusters = operations.clustering(startedAt, vectorizedPages)
	operations.evaluation(vectorizedPages, computedClusters)

if __name__ == '__main__':
	try:
		multiprocessing.log_to_stderr()
		logger = multiprocessing.get_logger()
		logger.setLevel(logging.INFO)
		test_1 = multiprocessing.Process(name = 'Test Dataset TMDB', target = testPipeline, args=("Dataset_TMDB",))
		test_2 = multiprocessing.Process(name = 'Test Dataset Study', target = testPipeline, args=("Dataset_Study",))
		test_3 = multiprocessing.Process(name = 'Test Dataset G2R', target = testPipeline, args=("Dataset_G2R",))
		tests = [test_1, test_2, test_3]
		for test in tests:
			test.start()
		for test in tests:
			test.join()
		print("Test Executed without exceptions")
	except Exception as e:
		print(e)
