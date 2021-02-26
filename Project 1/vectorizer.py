from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer:
    
    def fit_transform(self, html):

        vectorizer = TfidfVectorizer(stop_words = "english", max_df = 0.80)
        vectors = vectorizer.fit_transform(html)
        vectorizedHTML = []

        for i in range(0, len(html)):
            element = vectors.getrow(i).tocoo()
            vectorizedHTML.append({key: value for key, value in zip(element.col, element.data)})

        for i in range(0, len(vectorizedHTML)):
            for key, value in vectorizer.vocabulary_.items():
                if(value in vectorizedHTML[i].keys()):
                    vh = vectorizedHTML[i]
                    vh[key] = vh[value]
                    del vh[value]
                    vectorizedHTML[i] = vh
        
        for i in range(0, len(vectorizedHTML)):
            vh = vectorizedHTML[i]
            vh = {key: value for key, value in sorted(vh.items(), key=lambda item: item[1], reverse = True)}
            vectorizedHTML[i] = vh

        return vectorizedHTML