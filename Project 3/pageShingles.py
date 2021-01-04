from vectorizer import shingleVectorizer
from bs4 import BeautifulSoup

#SHINGLE_LEN is defined as 10 using Vertex authors' advice

SHINGLE_LEN = 10

class PageShingles:

    # Input: path and directory
    # Support functions: shingleVectorizer, takes as input the shingles found in webapage's tags. 
    #                    The webpage is read from file and given to tag extractor function.
    # Ouput: New PageShingles Class 


    def __init__(self, pathToFile, directory):

        self.directory = directory
        file =  open(pathToFile, "r", encoding="UTF-8")
        self.name = pathToFile.replace("pages\\","").replace(directory + "\\", "").replace("The Movie Database (TMDb).html","")
        
        content = file.read()
        tags = self.extractTags(content)
        shingles = self.findShingles(tags)
        self.shingleVector =  tuple(shingleVectorizer(shingles))
        
        file.close()

    # Input: self
    # Output: string representation of PageShingles object, usefull when printing groups of webpages

    def __repr__(self):
        return "Webpage[{0}]".format(self.name)

    def __str__(self):
        return "Webpage[{0}]".format(self.name)

    # Input: Webpage
    # Support libraries: BeautifulSoup, used for webpage's tags retrieval
    # Output: Tags

    def extractTags(self, content):
        soup = BeautifulSoup(content, "html.parser")
        return [tag.name for tag in soup.find_all()]

    # Input: Webpage's tags
    # For Loop: defines shingle list and inserts this list inside shingles list. 
    # While Loop: for each step allowed insert a tag inside shingle list
    # Ouput: List of maps, each map associate a tuple with each shingle 

    def findShingles(self, tags):
        iterations = len(tags) - SHINGLE_LEN + 1
        if iterations <= 0:
            iterations = 1

        shingles = []
        start_index = 0
        for i in range(iterations):
            shingle = []
            current_step = 0
            while current_step < SHINGLE_LEN:
                shingle.append(tags[start_index + current_step])
                current_step += 1
            shingles.append(shingle)
            start_index += 1

        shingles = list(map(lambda l: tuple(l), shingles))

        return shingles