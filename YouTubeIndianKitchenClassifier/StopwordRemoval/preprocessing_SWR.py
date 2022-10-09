from nltk.corpus import stopwords
class RemoveStopWord:
    def __init__(self):
        pass 


    def RSW(self,data):
        self.data = data
        self.new_data = []
        for w in self.data.split():
            if w in stopwords.words('english'):
                self.new_data.append('')
            else:
                self.new_data.append(w)
        self.x=self.new_data[:]
        self.new_data.clear()
        return " ".join(self.x)
