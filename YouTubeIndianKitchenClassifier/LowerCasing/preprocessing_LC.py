class lowerCasing:
    def __init__(self):
        pass
    
    def LC(self,data):
        self.data = data
        self.data['commentText'] = self.data['commentText'].str.lower()
        return self.data