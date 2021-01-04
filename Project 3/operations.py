from pageShingles import PageShingles
from evaluation import f1, executionTime, precision, recall
from clusterAlgorithm import startAlgorithm
import os, time, re

# Input: None
# Ouput: Paths of webpages to cluster

def getPaths():
   filePaths = []
   for root, _, files in os.walk("pages"):
      for name in files:
         filePaths.append(os.path.join(root, name))
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

   print("STATS:\n")
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
   
   print("Clustering:\n %s seconds \n" .format(pagesClustered) % executionTime(time.time(), clusteringStartedAt))
   print("Total execution time:\n %s seconds \n" % executionTime(time.time(), startTime))
   return computedClusters

# Input: Vectorized pages and computed clustes
# Support functions: F1Score from metrics, it computes the F1 value
# Output: F1 Metric value ##TODO: implementare precision e recall

def evaluation(pages, computedClusters):
   groups = {}
   for page in pages:
      groups[page.directory] = []
   for page in pages:
      groups[page.directory].append(page)
   idealClusters = list(groups.values())

   precisionValue = precision(idealClusters, computedClusters)
   recallValue = recall(idealClusters, computedClusters)
   f1Value = f1(precisionValue, recallValue)
   print("Precision Metric value:\n {}\n".format(precisionValue))
   print("Recall Metric value:\n {}\n".format(recallValue))
   print("F1 Metric value:\n {}\n".format(f1Value))

