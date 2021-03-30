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
from sklearn.prepocessing import StandardScaler 
sc= StandardScaler()
X= sc.fit_transform(X)



# preperation of datasets for to learning and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2)



# categorizing the outputs
from tensorflow.keras.utils import to_categorical 
y_train= to_categorical(y_train)
y_test= to_categorical(y_test)



