from page import Page
from cluster import cluster
import os
import time
import re
from evaluation_metrics import f1score


def test_clustering():
   start_time = time.time()

   print("Start reading the directory...")

   filePaths = []
   for root, dirs, files in os.walk("pages"):
      for name in files:
         filePaths.append(os.path.join(root, name))

   print("Start loading the HTML content...")

   pages = []
   for path in filePaths:
      tokens = re.split("\\\\", path)
      page = Page(path, tokens[1])
      pages.append(page)


   print("Number of pages loaded:{0}\n".format(len(pages)))
   print("--- Vectorizing pages execution time: %s seconds ---\n" % (time.time() - start_time))


   start_time_execution = time.time()

   print("---CLUSTERING RESULTS---\n")
   size = 0
   computed_clusters = cluster(pages)
   for group in computed_clusters:
      print(group)
      size += len(group)

   print("\n")
   print("Number of pages processed:{0}".format(size))
   print("--- Clustering execution time: %s seconds ---" % (time.time() - start_time_execution))
   print("--- Total execution time: %s seconds ---" % (time.time() - start_time))


   groups = {}
   for page in pages:
      groups[page.directory] = []

   for page in pages:
      groups[page.directory].append(page)

   true_clusters = list(groups.values())

   f1 = f1score(true_clusters,computed_clusters)

   print("f1-score:{}\n".format(f1))


if __name__ == '__main__':
   test_clustering()
