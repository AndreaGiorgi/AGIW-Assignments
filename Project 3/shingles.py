from vectorizer import shingleVectorizer
from bs4 import BeautifulSoup

SHINGLE_SIZE = 10

class ShinglesOnlyPage:

    # Input: path and directory
    # Support functions: shingleVectorizer, takes as input the shingles found in webapage's tags. 
    #                    The webpage is read from file and given to tag extractor function.
    # Ouput: New ShinglesOnlyPage Class 


    def __init__(self, pathToFile, directory):
        #read the html file

        self.directory = directory
        file =  open(pathToFile,"r",encoding="utf8")
        self.name = pathToFile.replace("pages\\","").replace(directory + "\\", "").replace("The Movie Database (TMDb).html","")
        content = file.read()
        file.close()

        #extract the tags ordered
        tags = self.extract_tags(content)

        #each contiguous sequence of 10 tags within the page
        shingles = self.find_shingles(tags)

        #the hash vector of the shingles
        self.shingle_vector =  tuple(shingleVectorizer(shingles))

    # Input: Webpage
    # Support libraries: BeautifulSoup, used for webpage's tags retrieval
    # Output: Tags

    def extract_tags(self, content):
        soup = BeautifulSoup(content, "html.parser")
        return [tag.name for tag in soup.find_all()]

    # Input: Webpage's tags
    # Ouput: List of maps, each map associate a tuple with each shingle 

    def find_shingles(self, tags):
        iterations = len(tags) - SHINGLE_SIZE+1
        if iterations <= 0:
            iterations = 1

        shingles = []
        start_index = 0
        for i in range(iterations):
            shingle = []
            current_step = 0
            while current_step < SHINGLE_SIZE:
                shingle.append(tags[start_index + current_step])
                current_step += 1
            shingles.append(shingle)
            start_index += 1

        shingles = list(map(lambda l: tuple(l), shingles))

        return shingles