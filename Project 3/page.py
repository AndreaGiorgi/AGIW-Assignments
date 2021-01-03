from vectorize_shingle import shingles_to_vectors
from bs4 import BeautifulSoup

SHINGLE_SIZE = 10

class Page:
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
        self.shingle_vector =  tuple(shingles_to_vectors(shingles))

    def __repr__(self):
        return "Page({0})".format(self.name)

    def __str__(self):
        return "Page({0})".format(self.name)


    def extract_tags(self, content):
        soup = BeautifulSoup(content, "html.parser")
        #the list of tags within the page ordered
        return [tag.name for tag in soup.find_all()]

    def find_shingles(self, tags):
        iterations = len(tags)- SHINGLE_SIZE+1
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

