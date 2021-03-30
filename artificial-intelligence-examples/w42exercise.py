# importing libraries
import numpy as np 
import pandas as pd 


# loading dataset
data= pd.read_csv('phone_data.csv')


# class specification
from sklearn.preprocessing import LabelEncoder

label_encoder= LabelEncoder().fit(data.price_range)
labels= label_encoder.transform(data.price_range) 
classes= list(label_encoder.classes_)

X= data.drop(['price_range'], axis=1)
y= labels


# standardization of datasets
from sklearn.prerpocessing import StandardScaler 
sc= StandardScaler()
X= sc.fit_transform(X)
