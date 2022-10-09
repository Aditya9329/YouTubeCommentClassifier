class PunctuationRemover:
    def __init__(self):
        pass 
    def PR(self,data):
        self.data = data
        self.punc='"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        for e in self.punc:
            self.data = self.data.replace(e,'')
        return self.data 