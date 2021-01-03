from evaluation import Evaluation
import os
from lxml import html
from vectorizer import Vectorizer
from pageAllignament import PageAllignament

class PageFetcher:
    
    def fetchPages(self,pagePath,webSite):
        xpath = "//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()"
        pages = []
        path = os.path.join(pagePath, webSite)
        files = sorted(os.listdir(path))[:50]
        
        for filename in files:
            filename = os.path.join(path,filename)
            file = open(filename, "r", encoding="UTF-8")
            page = file.read()
            tree = html.fromstring(page)
            htmlLeaves = tree.xpath(xpath)
            page = ""
            for leaf in htmlLeaves:
                page = page + " " + leaf
            pages.append(page)

        return pages

class Project:

    def startAnalysis(self, folder, S1_path, S2_path):

        fetcher = PageFetcher()
        S1 = fetcher.fetchPages(folder, S1_path)
        S2 = fetcher.fetchPages(folder, S2_path)

        #We use a document representation based on TF-IDF model
        TF_IDF = Vectorizer()
        S1_HTML = TF_IDF.fit_transform(S1)
        S2_HTML = TF_IDF.fit_transform(S2)
        pageAllignament = PageAllignament()
        S1S2_Pairs = pageAllignament.allignSources(S1_HTML, S2_HTML)
    
        print("Stats of: " + str(S1_path) + " and " + str(S2_path))
        evaluation = Evaluation()
        evaluation.eval(S1S2_Pairs)

project = Project()

project.startAnalysis('dataset', 'NBA', 'ROTOWORLD')
project.startAnalysis('dataset', 'NBA', 'REALGM')
project.startAnalysis('dataset', 'ROTOWORLD', 'REALGM')