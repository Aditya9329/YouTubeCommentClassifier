import csv

import io 

from lzma import MF_BT2
from turtle import update
# from cv2 import resize
from django.shortcuts import render

from django.http import HttpResponse

from LowerCasing import preprocessing_LC

from RemoveSpecialCharacter import preprocessing_RSC

from RemovePunctuation import preprocessing_RP 

from StopwordRemoval import preprocessing_SWR

from DataTransformation import preprocessing_TRFM

from . import forms

import pickle 

import pandas as pd 

d = {
    'commentText':['Hello','H...i','How ,,?@are you','Good']
}
# data = pd.DataFrame(d,columns=['commentText'])


def home(request):
    # data = pd.DataFrame(columns=['commentText'])
    # print(data.shape)
    if request.method =='POST':
        mf = request.FILES.get('upload_file')
        decoded_file = mf.read().decode('latin-1').splitlines()
        L = []
        for line in decoded_file:
            L.append(line)
            # print(line)
        
        # print(decoded_file)
        print(L)


        data = pd.DataFrame({'commentText':L})
        print(data)


         # apply preprocessing for lowercasing the text from the corpus
        updated_data = preprocessing_LC.lowerCasing().LC(data)
        # print(updated_data)

        # apply preprocessing for removing the special characters from the corpus
        updated_data['commentText'] = updated_data['commentText'].apply(preprocessing_RSC.specialCharacterRemover().sCR)


        # apply preprocessing for removing the punctuation from the corpus
        updated_data['commentText'] = updated_data['commentText'].apply(preprocessing_RP.PunctuationRemover().PR)
        # print(updated_data)


         # apply preprocessing for removing the stopwords from the corpus
        updated_data['commentText'] = updated_data['commentText'].apply(preprocessing_SWR.RemoveStopWord().RSW)


        data_to_model = preprocessing_TRFM.TextTransformation().Vectorization(updated_data)
        print(data_to_model)


        machine  = pickle.load(open('./model/multi2.sav','rb'))
        result = machine.predict(data_to_model)
        

        # vect = pickle.load(open('./model/cv2.sav','rb')) 
        # n= vect.transform(self.data['commentText']).toarray()
        # return n






        # file = request.FILES['file'] 
        # decoded_file = file.read().decode('utf-8').splitlines()
        # reader = csv.DictReader(decoded_file)
        # for row in reader:
        #         # Get each cell value based on key-value pair. 
        #         # Key will always be what lies on the first row.      
    
        return HttpResponse(result)
    else:
        form = forms.File()
        res =render(request,'index.html',{'form':form}) 
        return res




# def test(request):
#     if request.method =='POST':
#         data = request.FILES['data']
#         print(data)
#     return HttpResponse("file is working")

# def test1(request):
    
    # apply preprocessing for lowercasing the text from the corpus
    # updated_data = preprocessing_LC.lowerCasing().LC(data)


    # apply preprocessing for removing the special characters from the corpus
    # updated_data['commentText'] = updated_data['commentText'].apply(preprocessing_RSC.specialCharacterRemover().sCR)

    # apply preprocessing for removing the punctuation from the corpus
    # updated_data['commentText'] = updated_data['commentText'].apply(preprocessing_RP.PunctuationRemover().PR)
    # print(updated_data)

    # apply preprocessing for removing the stopwords from the corpus
    # updated_data['commentText'] = updated_data['commentText'].apply(preprocessing_SWR.RemoveStopWord().RSW)
    # print(updated_data)
    # performing the vectorization
    # data_to_model = preprocessing_TRFM.TextTransformation().Vectorization(updated_data)
    # print(data_to_model)
    # return HttpResponse("Hey , i am working properly")


