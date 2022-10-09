import re

class specialCharacterRemover:
    def __init__(self):
        pass

    # def sCR(self,data):
    #     self.data = data
    #     self.data['commentText'] = re.sub(r"[^a-zA-Z0-9 ]", "", self.data['commentText'])
    #     return self.data

    def sCR(self,data):
        self.data = data
        self.data = re.sub(r"[^a-zA-Z0-9 ]", "", self.data)
        return self.data