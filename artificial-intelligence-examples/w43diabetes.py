# importing essential libraries
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 


# reading data's
data = pd.read_csv('diabetes.csv')


# class specification
label_encoder= LabelEncoder().fit(data.output)
labels= label_encoder.transform(data.output)
classes= list(label_encoder.classes_)

X= data.drop(['output'], axis=1)   
y= labels

