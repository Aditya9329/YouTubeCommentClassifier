from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

class Stemmer:
    def __init__(self):
        pass 


    def ST(self,data):
        self.data = data
        self.y=[]
        for e in self.data:
            self.y.append(ps.stem(e))
        self.z=self.y[:]
        self.y.clear() 
        return self.z 