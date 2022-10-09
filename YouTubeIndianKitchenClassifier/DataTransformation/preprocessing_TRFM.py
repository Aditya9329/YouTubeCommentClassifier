from sklearn.feature_extraction.text import CountVectorizer 
# cv = CountVectorizer(max_features=500)
import pandas as pd 
import pickle

class TextTransformation:
    def __init__(self):
        pass 

    def Vectorization(self,data):
        self.data = data
        vect = pickle.load(open('./model/cv2.sav','rb')) 
        n= vect.transform(self.data['commentText']).toarray()
        return n