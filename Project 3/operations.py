from shingles import Shingles
from evaluation_metrics import executionTime, f1score
from cluster import cluster
import os, time, re

# Input: None
# Ouput: Paths of webpages to cluster

def initialization():

   filePaths = []
   for root, dirs, files in os.walk("pages"):
      for name in files:
         filePaths.append(os.path.join(root, name))

   return filePaths

# Input: execution starting time and webpages paths
# Support libraries: re for split operation on each path ##TODO: spiegare bene
# Support class: Page ##TODO: spiegare cos'è la classe page
# Ouput: Vectorized pages and execution time stats

def vectorization(startTime, filePaths):
   pages = []
   for path in filePaths:
      tokens = re.split("\\\\", path)
      pageShingles = Shingles(path, tokens[1])
      pages.append(pageShingles)

   vectorizingFinishedAt = time.time()

   print("Vectorization completed in: %s seconds \n" % executionTime(vectorizingFinishedAt, startTime))
   return pages

# Input: execution starting time and vectorized pages
# Support function: cluster, it defines the operation needed in order to cluster all pages
# Output: Computed clusters and execution time stats

def clustering(startTime, pages):

   clusteringStartedAt = time.time()
   computedClusters = cluster(pages)

   # print(group) in for loop if you want to see all created groups

   pagesClustered = 0
   for group in computedClusters:
      pagesClustered += len(group)

   print("Clustering of {0} pages completed in: %s seconds \n" .format(pagesClustered) % executionTime(time.time(), clusteringStartedAt))
   print("Total execution time: %s seconds \n" % executionTime(time.time(), startTime))
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

   true_clusters = list(groups.values())

   f1 = f1score(true_clusters, computedClusters)

   print("F1 Metric value: {}\n".format(f1))

