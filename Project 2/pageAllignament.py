class PageAllignament:

    def intersect(self, S1_labels, S2_labels):
            
        intersections = 0
        for label1 in S1_labels:
            for label2 in S2_labels:
                if(label1 == label2):
                    intersections += 1            
        
        return intersections


    def allignSources(self, S1, S2):

        pairs = []
        for i in range(0, len(S1)):
            elementS1 = S1[i]
            matches = []
            filteredS1 = self.filter(elementS1, 0.05)

            for j in range(0, len(S2)):
                elementS2 = S2[j]
                filteredS2 = self.filter(elementS2, 0.05)
                matches.append(self.intersect(filteredS1, filteredS2))
            maxMatch = max(matches)
            
            # If maxMatch is more than one it means that at least one label match has been found
            if maxMatch > 1:
                pairs.append((i, matches.index(maxMatch)))

        return pairs

    def filter(self, S, minValue):
        # Filters Source elements by frequency
        values = []
        for key,_ in S.items():
            if(S[key] > minValue):
                values.append(key)
        return values