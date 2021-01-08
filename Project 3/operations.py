from pageShingles import PageShingles
from evaluation import evaluationPipeline, executionTime
from clusterAlgorithm import startAlgorithm
import os, time, re

# Input: None
# Ouput: Paths of webpages to cluster

def getPaths(path):
   filePaths = []
   numPagesFound = 0
   for root, _, files in os.walk(path):
      for name in files:
         filePaths.append(os.path.join(root, name))
         numPagesFound += 1

   print("Execution Statistics of :" + path)
   print("\n Loaded from " + path +":\n %s pages \n" % numPagesFound)
   return filePaths

# Input: execution starting time and webpages paths
# Support libraries: re for split operation on each path 
# Support class: PageShingles, it's a class which defines a page composed by only shingles
# Ouput: Vectorized pages and execution time stats

def vectorization(startTime, filePaths):
   pages = []
   for path in filePaths:
      tokens = re.split("\\\\", path)
      shinglePage = PageShingles(path, tokens[1])
      pages.append(shinglePage)
   vectorizingFinishedAt = time.time()

   print("Vectorization:\n %s seconds \n" % executionTime(vectorizingFinishedAt, startTime))
   return pages

# Input: execution starting time and vectorized pages
# Support function: cluster, it defines the operation needed in order to cluster all pages
# Output: Computed clusters and execution time stats

def clustering(startTime, pages):
   clusteringStartedAt = time.time()
   pagesClustered = 0
   computedClusters = startAlgorithm(pages)
   for group in computedClusters:
      pagesClustered += len(group)
   
   print("Pages Processed: \n %s \n" % format(pagesClustered))
   print("Clustering:\n %s seconds \n" % executionTime(time.time(), clusteringStartedAt))
   print("Total execution time:\n %s seconds \n" % executionTime(time.time(), startTime))
   return computedClusters

# Input: Vectorized pages and computed clustes
# Support functions: F1Score from metrics, it computes the F1 value
# Output: F1 Metric value

def evaluation(pages, computedClusters):
   groups = {}
   for page in pages:
      groups[page.directory] = []
   for page in pages:
      groups[page.directory].append(page)
   idealClusters = list(groups.values())
   evaluationPipeline(idealClusters, computedClusters)


