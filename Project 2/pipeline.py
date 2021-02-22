from vectorizer import Vectorizer
from pageFetcher import PageFetcher
from pageAllignament import PageAllignament
from evaluation_pipeline import evaluation_pipeline


def startAnalysis(folder, S1_path, S2_path):

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
        evaluation_pipeline(S1S2_Pairs)


def pipeline():
    startAnalysis('dataset', 'NBA', 'ROTOWORLD')
    startAnalysis('dataset', 'NBA', 'REALGM')
    startAnalysis('dataset', 'ROTOWORLD', 'REALGM')
    

if __name__ == '__main__':
    pipeline()
    